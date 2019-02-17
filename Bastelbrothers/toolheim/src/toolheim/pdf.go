package toolheim

import (
	"strconv"
    "math"
	"github.com/jung-kurt/gofpdf"
)

func MakePDF(warband Warband) {
	pdf := gofpdf.New("P", "mm", "A4", "")
	pdf.AddPage()

	pdf.SetTextColor(170, 0, 0)

	pdf.SetFont("Arial", "B", 30)
	pdf.SetXY(5, 5)
	pdf.Write(11, warband.Warband.Name)
	pdf.SetFont("Arial", "B", 17)
	pdf.SetXY(5, 13)
	pdf.Write(11, warband.Warband.Race)

	offsetYHeader := 22
	offsetY := 0
    henchmen_cnt := 0
    hero_cnt := 0

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
		pdf.SetFont("Arial", "B", 15)
		pdf.SetY(float64(offsetY + 4))
		pdf.SetX(20)
		pdf.Write(11, hero.Name)

		// Type
		pdf.SetFont("Arial", "", 13)
		pdf.SetY(float64(offsetY + 11))
		pdf.SetX(20)
		pdf.Write(11, hero.Type)

		// Stats
		pdf.SetFillColor(255, 0, 0)
		pdf.SetFont("Arial", "B", 13)
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
		pdf.SetX(58.5)
		pdf.Write(11, strconv.Itoa(hero.Stats.Leadership))

		// Weapons
		pdf.SetFont("Arial", "B", 12)
		pdf.SetXY(138, float64(offsetY+6))
		pdf.Write(11, hero.Weapons.MainHand)
		pdf.SetFont("Arial", "", 12)
		pdf.SetXY(138, float64(offsetY+11))
		pdf.Write(11, hero.Weapons.OffHand)

		// Armour
		pdf.SetFont("Arial", "", 11)
		if hero.Armour != nil {
			for j, armour := range hero.Armour.List {
				pdf.SetXY(170, float64(offsetY+6+(j*5)))
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

        hero_cnt = hero_cnt + 1
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

		pdf.SetFont("Arial", "B", 15)
		// Name
		pdf.SetY(float64(offsetY + 4))
		pdf.SetX(18)
		pdf.Write(11, henchmen.Name)

		// Type
		pdf.SetFont("Arial", "", 13)
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

		pdf.SetFont("Arial", "B", 13)
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
		pdf.SetX(58.5)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Leadership))

		// Weapons
		pdf.SetFont("Arial", "B", 12)
		pdf.SetXY(138, float64(offsetY+7))
		pdf.Write(11, henchmen.Weapons.MainHand)
		pdf.SetFont("Arial", "", 12)
		pdf.SetXY(138, float64(offsetY+12))
		pdf.Write(11, henchmen.Weapons.OffHand)

		// Armour
		pdf.SetFont("Arial", "", 11)
		if henchmen.Armour != nil {
			for j, armour := range henchmen.Armour.List {
				pdf.SetXY(170, float64(offsetY+7+(j*5)))
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
		pdf.SetFont("Arial", "B", 13)
		pdf.SetXY(190, float64(offsetY+21))
		pdf.Write(20, strconv.Itoa(henchmen.Experience))

        henchmen_cnt = henchmen_cnt + henchmen.Number
	}

	// Statistic page
	pdf.AddPage()
	startY = 0
    offsetY = 0
	pdf.SetFont("Arial", "B", 13)
	pdf.SetXY(20, float64(offsetY+21))
	pdf.Write(20, strconv.Itoa(warband.Rating))

    offsetY = offsetY + 20
    pdf.SetFont("Arial", "B", 13)
    pdf.SetXY(20, float64(offsetY+21))
    pdf.Write(20, strconv.Itoa(hero_cnt))

    offsetY = offsetY + 20
    pdf.SetFont("Arial", "B", 13)
    pdf.SetXY(20, float64(offsetY+21))
    pdf.Write(20, strconv.Itoa(len(warband.HenchmenGroups)))

    offsetY = offsetY + 20
    pdf.SetFont("Arial", "B", 13)
    pdf.SetXY(20, float64(offsetY+21))
    pdf.Write(20, strconv.Itoa(henchmen_cnt))

    routtest := int(math.RoundToEven(float64(hero_cnt + henchmen_cnt) / 4.0))

    offsetY = offsetY + 20
    pdf.SetFont("Arial", "B", 13)
    pdf.SetXY(20, float64(offsetY+21))
    pdf.Write(20, strconv.Itoa(routtest))

    offsetY = offsetY + 20
    pdf.SetFont("Arial", "B", 13)
    pdf.SetXY(20, float64(offsetY+21))
    pdf.Write(20, strconv.Itoa(warband.CampaignPoints))

	// TODO: Make output name variable or use name of the input file
	err := pdf.OutputFileAndClose("warband-roaster.pdf")

	if err != nil {
		panic(err)
	}
}
