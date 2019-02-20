package toolheim

import (
	"math"
	"strconv"
	//"fmt"
	"github.com/jung-kurt/gofpdf"
)

func MakePDF(warband Warband) {
	pdf := gofpdf.New("P", "mm", "A4", "")
	pdf.AddPage()

	pdf.SetTextColor(170, 0, 0)

	pdf.SetFont("Arial", "B", 28)
	pdf.SetXY(5, 5)
	pdf.Write(11, warband.Warband.Name)
	pdf.SetFont("Arial", "B", 17)
	pdf.SetXY(5, 13)
	pdf.Write(11, warband.Warband.Race)

	offsetYHeader := 22
	offsetY := 0
	henchmen_sum_xp := 0
	henchmen_cnt := 0
	hero_sum_xp := 0
	hero_cnt := 0
	hiredsword_sum_xp := 0
	hiredsword_cnt := 0
	large_cnt := 0

	for i, hero := range warband.Heros {
		posY := 43
		offsetY = i*posY + offsetYHeader

		if offsetY > 297-40 {
			pdf.AddPage()
			offsetY = 0
		}
		// Background
		pdf.SetX(5)
		pdf.SetY(float64(offsetY + 5))
		pdf.Image("images/hero.png", 5, 0, 1499*0.133, 295*0.133, true, "", 0, "")

		// Name
		pdf.SetFont("Arial", "B", 12)
		pdf.SetY(float64(offsetY + 4))
		pdf.SetX(18)
		pdf.Write(11, hero.Name)

		// Type
		pdf.SetFont("Arial", "", 12)
		pdf.SetY(float64(offsetY + 10))
		pdf.SetX(18)
		pdf.Write(11, hero.Type)

		// Stats
		pdf.SetFillColor(255, 0, 0)
		pdf.SetFont("Arial", "", 13)
		pdf.SetFontUnitSize(5)

		pdf.SetY(float64(offsetY + 24))
		pdf.SetX(6)
		pdf.Write(11, strconv.Itoa(hero.Stats.Movement))
		pdf.SetX(13)
		pdf.Write(11, strconv.Itoa(hero.Stats.WeaponSkill))
		pdf.SetX(20)
		pdf.Write(11, strconv.Itoa(hero.Stats.BallisticSkill))
		pdf.SetX(27)
		pdf.Write(11, strconv.Itoa(hero.Stats.Strength))
		pdf.SetX(33)
		pdf.Write(11, strconv.Itoa(hero.Stats.Toughness))
		pdf.SetX(40)
		pdf.Write(11, strconv.Itoa(hero.Stats.Wounds))
		pdf.SetX(46)
		pdf.Write(11, strconv.Itoa(hero.Stats.Initiative))
		pdf.SetX(53)
		pdf.Write(11, strconv.Itoa(hero.Stats.Attacks))
		pdf.SetX(59.5)
		pdf.Write(11, strconv.Itoa(hero.Stats.Leadership))
		pdf.SetX(66.0)
		pdf.Write(11, strconv.Itoa(hero.Stats.Save))

		// Skill lists
		if hero.bSkillLists.Combat == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(7.25, float64(offsetY + 21))
			pdf.Write(0, "X")
		}
		if hero.bSkillLists.Shooting == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(17.75, float64(offsetY + 21))
			pdf.Write(0, "X")
		}
		if hero.bSkillLists.Academic == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(28.72, float64(offsetY + 21))
			pdf.Write(0, "X")
		}
		if hero.bSkillLists.Strength == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(40.5, float64(offsetY + 21))
			pdf.Write(0, "X")
		}
		if hero.bSkillLists.Speed == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(51.5, float64(offsetY + 21))
			pdf.Write(0, "X")
		}
		if hero.bSkillLists.Special == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(60.7, float64(offsetY + 21))
			pdf.Write(0, "X")
		}

		// Weapons
		if hero.Weapons != nil {
			for w, weapon := range hero.Weapons.List {
				if w == 0 {
					pdf.SetFont("Arial", "B", 10)
				} else {
					pdf.SetFont("Arial", "", 10)
				}
				pdf.SetXY(138, float64(offsetY + 7 + (w * 5)))
				pdf.Write(11, weapon)
			}
		}

		// Armour
		pdf.SetFont("Arial", "", 10)
		if hero.Armour != nil {
			for j, armour := range hero.Armour.List {
				pdf.SetXY(168, float64(offsetY+3+(j*5)))
				pdf.Write(11, armour)
			}
		}

		if hero.Rules != nil {
			for j, rule := range hero.Rules.List {
				pdf.SetXY(75, float64(offsetY+6+(j*5)))
				pdf.Write(11, rule)
			}
		}

		// XP
		pdf.SetFont("Arial", "B", 20)
		pdf.SetXY(185, float64(offsetY+28))
		pdf.Write(20, strconv.Itoa(hero.Experience))
		y := 0.0
		reduce_x := 0
		for x := 1; x <= hero.Experience; x++ {
			pdf.SetFont("Arial", "B", 10)
			xx := x
			if reduce_x > 0 {
				xx = xx - reduce_x*30
			}
			pdf.SetXY(float64(73+((float64(xx)-1.0)*3.43)), float64(offsetY)+float64(y)*15.0+34.0)
			pdf.Write(0, "X")
			if x == 30 || x == 60 {
				y = y + 0.22
				reduce_x = reduce_x + 1
			}
		}

		if !hero.Large && !hero.HiredSword {
			hero_sum_xp = hero_sum_xp + hero.Experience
			hero_cnt = hero_cnt + 1
		} else if hero.Large {
			hero_sum_xp = hero_sum_xp + hero.Experience
			large_cnt = large_cnt + 1
		} else if hero.HiredSword {
			hiredsword_sum_xp = hiredsword_sum_xp + hero.Experience
			hiredsword_cnt = hiredsword_cnt + 1
		}

	}

	startY := offsetY + 50
	if startY > 297-60 {
		pdf.AddPage()
		startY = 0
	}

	for i, henchmen := range warband.HenchmenGroups {
		posY := 32
		offsetY = i*posY + startY

		// Background
		pdf.SetX(5)
		pdf.SetY(float64(offsetY + 5))
		pdf.Image("images/henchmen.png", 5, 0, 1499*0.133, 218*0.133, true, "", 0, "")

		pdf.SetFont("Arial", "B", 12)
		// Name
		pdf.SetY(float64(offsetY + 4))
		pdf.SetX(18)
		pdf.Write(11, henchmen.Name)

		// Type
		pdf.SetFont("Arial", "", 12)
		pdf.SetY(float64(offsetY + 9))
		pdf.SetX(18)
		pdf.Write(11, henchmen.Type)

		// Number
		pdf.SetFont("Arial", "B", 12)
		pdf.SetY(float64(offsetY + 9))
		pdf.SetX(64)
		pdf.Write(11, strconv.Itoa(henchmen.Number))

		// Stats
		pdf.SetFillColor(255, 0, 0)

		pdf.SetFont("Arial", "", 12)
		pdf.SetFontUnitSize(5)

		pdf.SetY(float64(offsetY + 18))
		pdf.SetX(6)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Movement))
		pdf.SetX(13)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.WeaponSkill))
		pdf.SetX(20)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.BallisticSkill))
		pdf.SetX(27)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Strength))
		pdf.SetX(33)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Toughness))
		pdf.SetX(40)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Wounds))
		pdf.SetX(46)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Initiative))
		pdf.SetX(53)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Attacks))
		pdf.SetX(59.5)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Leadership))
		pdf.SetX(66.0)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Save))

		// Weapons
		if henchmen.Weapons != nil {
			for w, weapon := range henchmen.Weapons.List {
				if w == 0 {
					pdf.SetFont("Arial", "B", 10)
				} else {
					pdf.SetFont("Arial", "", 10)
				}
				pdf.SetXY(138, float64(offsetY+7+(w*5)))
				pdf.Write(11, weapon)
			}
		}

		// Armour
		pdf.SetFont("Arial", "", 10)
		if henchmen.Armour != nil {
			for j, armour := range henchmen.Armour.List {
				pdf.SetXY(170, float64(offsetY+3+(j*5)))
				pdf.Write(11, armour)
			}
		}

		// Rules
		if henchmen.Rules != nil {
			for j, rule := range henchmen.Rules.List {
				pdf.SetXY(75, float64(offsetY+7+(j*5)))
				pdf.Write(11, rule)
			}
		}

		// XP
		pdf.SetFont("Arial", "", 13)
		pdf.SetXY(190, float64(offsetY+21))
		pdf.Write(20, strconv.Itoa(henchmen.Experience))
		for x := 1; x <= henchmen.Experience; x++ {
			pdf.SetFont("Arial", "B", 12)
			pdf.SetXY(float64(137+((float64(x)-1.0)*3.45)), float64(offsetY)+30.5)
			pdf.Write(0, "X")
		}

		if !henchmen.Large {
			henchmen_sum_xp = henchmen_sum_xp + (henchmen.Experience * henchmen.Number)
			henchmen_cnt = henchmen_cnt + henchmen.Number
		} else {
			henchmen_sum_xp = henchmen_sum_xp + (henchmen.Experience * henchmen.Number)
			large_cnt = large_cnt + 1
		}
	}

	// Statistic page
	pdf.AddPage()
	startY = 0
	offsetY = 0

	// Campaign status
	pdf.SetX(5)
	pdf.SetY(5)
	pdf.Image("images/wb_stats.png", 5, 0, 1499*0.133, 218*0.133, true, "", 0, "")

	// Equipment
	pdf.SetFont("Arial", "", 10)
	offsetX := 0
	offsetY = 0
	if warband.Equipment != nil {
		for j, e := range warband.Equipment.List {
			pdf.SetXY(123 + float64(offsetX), float64(offsetY + 6 + (j * 5)))
			pdf.Write(11, e)
	if j == 4 {
	offsetX = 40
	offsetY = -25
	}
		}
	}

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(60, 32.0)
	pdf.Write(0, strconv.Itoa(warband.Rating))

	routtest := int(math.RoundToEven(float64(hero_cnt+henchmen_cnt) / 4.0))

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(72.5, 32.0)
	pdf.Write(0, "Routtest: ")
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(95, 32.0)
	pdf.Write(0, strconv.Itoa(routtest))

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(60, 11.25)
	pdf.Write(0, strconv.Itoa(hero_sum_xp))

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(60, 14.75)
	pdf.Write(0, strconv.Itoa(henchmen_sum_xp))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(22.05, 18.0)
	pdf.Write(0, strconv.Itoa(hero_cnt+henchmen_cnt+hiredsword_cnt))
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(60.0, 18.0)
	pdf.Write(0, strconv.Itoa((hero_cnt+henchmen_cnt+hiredsword_cnt) * 5))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(32.05, 21.25)
	pdf.Write(0, strconv.Itoa(large_cnt))
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(60.0, 21.25)
	pdf.Write(0, strconv.Itoa((large_cnt) * 20))

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(60.0, 24.5)
	pdf.Write(0, strconv.Itoa(hiredsword_sum_xp))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(95, 11.25)
	pdf.Write(0, strconv.Itoa(warband.GoldCrowns))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(95, 17.75)
	pdf.Write(0, strconv.Itoa(warband.Shards))

	// Warband general header
	pdf.SetXY(5, 40)
	pdf.Image("images/campaign.png", 5, 0, 1499*0.133, 218*0.133, true, "", 0, "")

/*
	pdf.SetFont("Arial", "B", 13)
	pdf.SetXY(20, float64(offsetY+21))
	pdf.Write(20, strconv.Itoa(hero_cnt))

	pdf.SetFont("Arial", "B", 13)
	pdf.SetXY(20, float64(offsetY+21))
	pdf.Write(20, strconv.Itoa(len(warband.HenchmenGroups)))

	pdf.SetFont("Arial", "B", 13)
	pdf.SetXY(20, float64(offsetY+21))
	pdf.Write(20, strconv.Itoa(henchmen_cnt))
*/

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(22, 46.25)
	pdf.Write(0, warband.Objective)

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(147, 60.0)
	pdf.Write(0, strconv.Itoa(warband.CampaignPoints))

	row := 0
	for x := 1; x <= warband.CampaignPoints; x++ {
		pdf.SetFont("Arial", "B", 8)
		xx := x - (row * 20)
		pdf.SetXY(float64(130.75+((float64(xx)-1.0)*3.30)), float64(64.4) + float64((float64(row) * float64(2.5))))
		pdf.Write(0, "X")
		if x == 20 {
			row = row + 1
		}
	}

/*
	routtest := int(math.RoundToEven(float64(hero_cnt+henchmen_cnt) / 4.0))

	offsetY = offsetY + 20
	pdf.SetFont("Arial", "B", 13)
	pdf.SetXY(20, float64(offsetY+21))
	pdf.Write(20, strconv.Itoa(hero_cnt+henchmen_cnt))

	pdf.SetFont("Arial", "B", 13)
	pdf.SetXY(40, float64(offsetY+21))
	pdf.Write(20, strconv.Itoa(routtest))

*/

	// TODO: Make output name variable or use name of the input file
	err := pdf.OutputFileAndClose("warband-roaster.pdf")

	if err != nil {
		panic(err)
	}
}
