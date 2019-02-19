package toolheim

import (
	"regexp"
	"strconv"
	"strings"
	"fmt"

	"github.com/davecgh/go-spew/spew"
	"github.com/ghodss/yaml"
)

type Warband struct {
	Warband        *WarbandName     `json:"warband"`
	Rating         int              `json:"rating"`
	CampaignPoints int              `json:"campaign"`
	GoldCrowns     int              `json:"gc"`
	Shards         int              `json:"shards"`
	Equipment      *ItemList        `json:"equipment"`
	Heros          []*Hero          `json:"heros"`
	HenchmenGroups []*HenchmenGroup `json:"henchmen"`
	Notes          []string         `json:"notes"`
	Objective		string			`json:"objective"`
}

type WarbandName struct {
	Name string
	Race string
}

type ItemList struct {
	List []string
}

type Hero struct {
	Header		string		`json:"hero"`
	Name		string
	Type		string
	Experience	int
	WarbandAddition	int		`json:"warbandaddition,omitempty"`
	Stats		*Stats		`json:"stats,omitempty"`
	Large		bool		`json:"large"`
	HiredSword	bool		`json:"hiredsword"`
	Weapons		*ItemList	`json:"weapons,omitempty"`
	Armour		*ItemList	`json:"armour,omitempty"`
	Rules		*ItemList	`json:"rules,omitempty"`
	SkillLists	*ItemList	`json:"skilllists,omitempty"`
	bSkillLists	Skilllist
}

type HenchmenGroup struct {
	Header     string `json:"group"`
	Name       string
	Number     int
	Type       string
	Experience int
	Large      bool      `json:"large"`
	Stats      *Stats    `json:"stats"`
	Weapons    *ItemList `json:"weapons"`
	Armour     *ItemList `json:"armour"`
	Rules      *ItemList `json:"rules"`
}

type Weapons struct {
	MainHand string
	OffHand  string
}

type Stats struct {
	Movement       int
	WeaponSkill    int
	BallisticSkill int
	Strength       int
	Toughness      int
	Wounds         int
	Initiative     int
	Attacks        int
	Leadership     int
}

type Skilllist struct {
	Strength	bool
	Academic	bool
	Combat		bool
	Shooting	bool
	Speed		bool
	Special		bool
}

func (stats *Stats) UnmarshalJSON(b []byte) error {
	regex := regexp.MustCompile(`"\s*M([0-9]+)\s*,\s*WS([0-9]+)\s*,\s*BS([0-9]+)\s*,\s*S([0-9]+)\s*,\s*T([0-9]+)\s*,\s*W([0-9]+)\s*,\s*I([0-9]+)\s*,\s*A([0-9]+)\s*,\s*Ld([0-9]+)\s*"`)
	matches := regex.FindStringSubmatch(string(b))
	stats.Movement, _ = strconv.Atoi(matches[1])
	stats.WeaponSkill, _ = strconv.Atoi(matches[2])
	stats.BallisticSkill, _ = strconv.Atoi(matches[3])
	stats.Strength, _ = strconv.Atoi(matches[4])
	stats.Toughness, _ = strconv.Atoi(matches[5])
	stats.Wounds, _ = strconv.Atoi(matches[6])
	stats.Initiative, _ = strconv.Atoi(matches[7])
	stats.Attacks, _ = strconv.Atoi(matches[8])
	stats.Leadership, _ = strconv.Atoi(matches[9])

	return nil
}

func (warband *WarbandName) UnmarshalJSON(b []byte) error {
	regex := regexp.MustCompile(`"([^\(]+)\(([^\)]+)\)`)
	matches := regex.FindStringSubmatch(string(b))
	warband.Name = strings.TrimSpace(matches[1])
	warband.Race = strings.TrimSpace(matches[2])
	return nil
}

func (itemList *ItemList) UnmarshalJSON(b []byte) error {
	items := strings.Split(string(b[1:len(b)-1]), ",")
	for _, item := range items {
		itemList.List = append(itemList.List, strings.TrimSpace(item))
	}
	return nil
}

func (hands *Weapons) UnmarshalJSON(b []byte) error {
	items := strings.Split(string(b[1:len(b)-1]), ",")
	hands.MainHand = strings.TrimSpace(items[0])
	if len(items) > 1 {
		hands.OffHand = strings.TrimSpace(items[1])
	}
	return nil
}

func ParseWarband(warbandDefinition []byte) Warband {
	var warband Warband

	err := yaml.Unmarshal(warbandDefinition, &warband)
	if err != nil {
		panic(err)
	}

	for _, h := range warband.Heros {
		regex := regexp.MustCompile(`([^\(]+)\(([^\)]+)\)\s*\[([0-9]+)XP\]\s*`)
		matches := regex.FindStringSubmatch(string(h.Header))
		h.Name = strings.TrimSpace(matches[1])
		h.Type = strings.TrimSpace(matches[2])
		h.Experience, _ = strconv.Atoi(strings.TrimSpace(matches[3]))
		if !h.Large {
			warband.Rating = warband.Rating + h.Experience + 5
		} else {
			warband.Rating = warband.Rating + h.Experience + 20
		}
		if h.WarbandAddition > 0 {
			warband.Rating = warband.Rating + h.WarbandAddition
		}
		// hier text Skill listen-Name zu boolschen Wert umwandeln
		fmt.Println(">>")
		fmt.Println(h.SkillLists.List)
		fmt.Println(h.bSkillLists)
		h.bSkillLists.Speed = false
        h.bSkillLists.Shooting = false
        h.bSkillLists.Special = false
        h.bSkillLists.Combat = false
        h.bSkillLists.Academic = false
        h.bSkillLists.Strength = false
		for _, s := range h.SkillLists.List {
			if strings.EqualFold(s, "Speed") {
				h.bSkillLists.Speed = true
			}
			if strings.EqualFold(s, "Shooting") {
				h.bSkillLists.Shooting = true
			}
			if strings.EqualFold(s, "Special") {
				h.bSkillLists.Special = true
			}
			if strings.EqualFold(s, "Combat") {
				h.bSkillLists.Combat = true
			}
			if strings.EqualFold(s, "Academic") {
				h.bSkillLists.Academic = true
			}
			if strings.EqualFold(s, "Strength") {
				h.bSkillLists.Strength = true
			}
		}
	}

	for _, hg := range warband.HenchmenGroups {
		regex := regexp.MustCompile(`([^\(]+)\(([0-9]+)x?\s+([^\)]+)\)\s*\[([0-9]+)XP\]\s*`)
		matches := regex.FindStringSubmatch(string(hg.Header))
		hg.Name = strings.TrimSpace(matches[1])
		hg.Number, _ = strconv.Atoi(strings.TrimSpace(matches[2]))
		hg.Type = strings.TrimSpace(matches[3])
		hg.Experience, _ = strconv.Atoi(strings.TrimSpace(matches[4]))
		if !hg.Large {
			warband.Rating = warband.Rating + (hg.Experience + 5) * hg.Number
		} else {
			warband.Rating = warband.Rating + (hg.Experience + 20) * hg.Number
		}

	}

	spew.Dump(warband)

	return warband
}
