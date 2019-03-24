package toolheim

import (
	"strconv"
	//"fmt"

	"github.com/jung-kurt/gofpdf"
)

var marker_sign  = "X"
var text_color_r = 170
var text_color_g = 0
var text_color_b = 0

var startY       = 0
var offsetY      = 0

func MakeHeroPage(warband Warband, pdf *gofpdf.Fpdf, newPage bool) {

	if !newPage {
	    // add a new page if required
		if startY > 297-60 {
			pdf.AddPage()
			startY = 0
			offsetY = 0
		}
	} else {
		pdf.AddPage()
		startY = 0
		offsetY = 0
	}

	shiftY := 44
	for i, hero := range warband.Heros {
		if i > 0 {
			offsetY = offsetY + shiftY
		}

		// handle multipage henchmen lists
		if offsetY > 297-60 {
			pdf.AddPage()
			offsetY = 0
		}

		// Background
		pdf.SetXY(5, float64(offsetY + 5))
		pdf.Image("images/hero.png", 5, 0, 1499*0.133, 295*0.133, true, "", 0, "")

		// Name
		pdf.SetFont("Arial", "B", 12)
		pdf.SetXY(18, float64(offsetY + 4))
		pdf.Write(11, hero.Name)

		// Type
		pdf.SetFont("Arial", "", 12)
		pdf.SetXY(18, float64(offsetY + 10))
		pdf.Write(11, hero.Type)

		// Stats
		pdf.SetFillColor(255, 0, 0)
		pdf.SetFont("Arial", "", 13)
		pdf.SetFontUnitSize(5)

		pdf.SetXY(6, float64(offsetY + 24))
		if len(hero.Stats.Movement) > 1 {
			pdf.SetX(3)
		}
		pdf.Write(11, hero.Stats.Movement)
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
		pdf.Write(11, hero.Stats.Save)

		// Skill lists
		if hero.bSkillLists.Combat == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(7.25, float64(offsetY + 21))
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Shooting == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(17.75, float64(offsetY + 21))
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Academic == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(28.72, float64(offsetY + 21))
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Strength == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(40.5, float64(offsetY + 21))
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Speed == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(51.5, float64(offsetY + 21))
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Special == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetXY(60.7, float64(offsetY + 21))
			pdf.Write(0, marker_sign)
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

		ox := 0
		oy := 0
		if hero.Rules != nil {
			for j, rule := range hero.Rules.List {
				pdf.SetXY(float64(75 + ox), float64(offsetY + 6 + (j * 5) + oy))
				pdf.Write(11, rule)
				if j == 3 {
					// start right of the first line after 4th line
					ox = 30
					oy = -20
				}
			}
		}

		if len(hero.Injuries) > 0 {
			pdf.SetFont("Arial", "", 7)
			pdf.SetXY(145, float64(offsetY + 27))
			pdf.Write(0, hero.Injuries)
		}

		if hero.HiredSword {
			// show hired sword marker
			pdf.SetXY(0, float64(offsetY) + 38.5)
			pdf.Image("images/hiredsword_marker.png", 6, 0, 421*0.053, 97*0.053, true, "", 0, "")
		}

		if hero.DramatisPersonae {
			// show dramatis personae marker
			pdf.SetXY(0, float64(offsetY) + 38.5)
			pdf.Image("images/dp_marker.png", 6, 0, 421*0.053, 97*0.051, true, "", 0, "")
		}

		if hero.Large {
			// show large creature marker
			pdf.SetXY(0, float64(offsetY) + 38.5)
			pdf.Image("images/large.png", 59.5, 0, 421*0.03, 97*0.05, true, "", 0, "")
		}

		// XP
		pdf.SetFont("Arial", "", 20)
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
			pdf.Write(0, marker_sign)
			if x == 30 || x == 60 {
				y = y + 0.22
				reduce_x = reduce_x + 1
			}
		}

	}

	offsetY = offsetY + shiftY

}

func MakeHenchmenPage(warband Warband, pdf *gofpdf.Fpdf, newPage bool) {

	if !newPage {
	    // add a new page if required
		if startY > 297-60 {
			pdf.AddPage()
			startY = 0
			offsetY = 0
		}
	} else {
		pdf.AddPage()
		startY = 0
		offsetY = 0
	}

	shiftY := 34
	for i, henchmen := range warband.HenchmenGroups {
		if i > 0 {
			offsetY = offsetY + shiftY
		}

		// handle multipage henchmen lists
		if offsetY > 297-60 {
			pdf.AddPage()
			offsetY = 0
		}

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

		if henchmen.Mount {
			// show mount marker
			pdf.SetXY(0, float64(offsetY) + 6.5)
			pdf.Image("images/mount.png", 58, 0, 421*0.033, 97*0.055, true, "", 0, "")
		}

		if henchmen.Large {
			// show large creature marker
			pdf.SetXY(0, float64(offsetY) + 28.2)
			pdf.Image("images/large.png", 58.5, 0, 421*0.03, 97*0.050, true, "", 0, "")
		}

		// Stats
		pdf.SetFillColor(255, 0, 0)

		pdf.SetFont("Arial", "", 12)
		pdf.SetFontUnitSize(5)

		pdf.SetY(float64(offsetY + 18))
		pdf.SetX(6)
		if len(henchmen.Stats.Movement) > 1 {
			pdf.SetX(3)
		}
		pdf.Write(11, henchmen.Stats.Movement)
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
		if len(henchmen.Stats.Save) > 1 {
			pdf.SetX(65.0)
		} else {
			pdf.SetX(66.0)
		}
		pdf.Write(11, henchmen.Stats.Save)

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
			pdf.Write(0, marker_sign)
		}

	}

}

func MakeStatisticPage(warband Warband, pdf *gofpdf.Fpdf) {

	// Statistic page
	pdf.AddPage()

	startY = 23
	offsetY = 0

	// First page warband heading
	pdf.SetFont("Arial", "B", 28)
	pdf.SetXY(5, 5)
	pdf.Write(11, warband.Warband.Name)
	pdf.SetFont("Arial", "B", 17)
	pdf.SetXY(5, 13)
	pdf.Write(11, warband.Warband.Race)

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(5, 20)
	pdf.Write(10, "Alignment: " + warband.Alignment)

	offsetY = 23

	// Warband status
	pdf.SetX(5)
	pdf.SetY(float64(offsetY)+5)
	pdf.Image("images/wb_stats.png", 5, 0, 1499*0.133, 218*0.133, true, "", 0, "")

	// Equipment
	pdf.SetFont("Arial", "", 10)
	oX := 0
	oY := 0
	if warband.Equipment != nil {
		for j, e := range warband.Equipment.List {
			pdf.SetXY(123 + float64(oX), float64(offsetY + oY + 6 + (j * 5)))
			pdf.Write(11, e)
			if j == 4 {
				oX = 40
				oY = -25
			}
		}
	}

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(55, float64(offsetY)+32.0)
	pdf.Write(0, strconv.Itoa(warband.Rating))

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(72.5, float64(offsetY)+32.0)
	pdf.SetTextColor(0, 0, 0)
	pdf.Write(0, "Routtest: ")
	pdf.SetFont("Arial", "", 10)
	pdf.SetTextColor(text_color_r, text_color_g, text_color_b)
	pdf.SetXY(93, float64(offsetY)+32.0)
	pdf.Write(0, strconv.Itoa(warband.routtest) + " (" + strconv.Itoa(warband.member_cnt) + ")")

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55, float64(offsetY)+11.25)
	pdf.Write(0, strconv.Itoa(warband.hero_sum_xp) + " (+" + strconv.Itoa(warband.wbAdd_sum - warband.dramatispersonae_sum_wbr) + ")" )

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55, float64(offsetY)+14.75)
	pdf.Write(0, strconv.Itoa(warband.henchmen_sum_xp))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(22.05, float64(offsetY)+18.0)
	pdf.Write(0, strconv.Itoa(warband.hero_cnt + warband.henchmen_cnt))
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55.0, float64(offsetY)+18.0)
	pdf.Write(0, strconv.Itoa((warband.hero_cnt + warband.henchmen_cnt) * 5))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(32.05, float64(offsetY)+21.25)
	pdf.Write(0, strconv.Itoa(warband.large_cnt))
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55.0, float64(offsetY)+21.25)
	pdf.Write(0, strconv.Itoa((warband.large_cnt) * 20))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(27.05, float64(offsetY)+24.5)
	pdf.Write(0, "( "+strconv.Itoa(warband.hiredsword_cnt)+" )")
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55.0, float64(offsetY)+24.5)
	pdf.Write(0, strconv.Itoa(warband.hiredsword_sum_xp) + " (+" + strconv.Itoa(warband.hiredsword_cnt * 5) + ")")

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(34.05, float64(offsetY)+28.0)
	pdf.Write(0, "( "+strconv.Itoa(warband.dramatispersonae_cnt)+" )")
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55.0, float64(offsetY)+28.0)
	pdf.Write(0, strconv.Itoa(warband.dramatispersonae_sum_wbr))

	if warband.mount_cnt > 0 {
		pdf.SetFont("Arial", "B", 10)
		pdf.SetXY(7.0, float64(offsetY)+36.25)
		pdf.Write(0, "Mounts: (" + strconv.Itoa(warband.mount_cnt) + ")")
		pdf.SetFont("Arial", "", 10)
		pdf.SetXY(55.0, float64(offsetY)+36.25)
		pdf.Write(0, strconv.Itoa((warband.mount_cnt) * 10))
	}

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(93, float64(offsetY)+11.25)
	pdf.Write(0, strconv.Itoa(warband.GoldCrowns))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(93, float64(offsetY)+17.75)
	pdf.Write(0, strconv.Itoa(warband.Shards))

	// Campaign info block
	offsetY = offsetY + 40
	pdf.SetXY(5, float64(offsetY))
	pdf.Image("images/campaign.png", 5, 0, 1499*0.133, 218*0.133, true, "", 0, "")

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(22, float64(offsetY)+6.25)
	pdf.Write(0, warband.Objective)

	// achievments block 
	pdf.SetFont("Arial", "", 10)
	lines := pdf.SplitLines([]byte(warband.Achievments), 190)
	ox := 0
	oy := 0
	for i := 0; i < len(lines); i++ {
		pdf.SetXY(float64(7.0 + ox), float64(offsetY + 14 + i * 5) + float64(oy))
		pdf.Write(0, string(lines[i]))
		if i == 2 {
			oy = oy - 18
			ox = ox + 55
		}
		if i == 6 {
			oy = oy - 20
			ox = ox + 55
		}
	}

	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(147, float64(offsetY)+20.0)
	pdf.Write(0, strconv.Itoa(warband.CampaignPoints))

	row := 0
	for x := 1; x <= warband.CampaignPoints; x++ {
		pdf.SetFont("Arial", "B", 8)
		xx := x - (row * 20)
		pdf.SetXY(float64(130.75+((float64(xx)-1.0)*3.30)), float64(offsetY)+float64(24.4) + float64((float64(row) * float64(2.5))))
		pdf.Write(0, marker_sign)
		if x == 20 {
			row = row + 1
		}
	}

	// Notes block 
	offsetY = offsetY + 35
	pdf.SetXY(5, float64(offsetY))
	pdf.Image("images/notes.png", 5, 0, 1499*0.133, 218*0.33, true, "", 0, "")

	pdf.SetFont("Arial", "", 10)
	lines = pdf.SplitLines([]byte(warband.Notes), 195)
	for i := 0; i < len(lines); i++ {
		pdf.SetXY(7.0, float64(offsetY + 7 + i * 5))
		pdf.Write(0, string(lines[i]))
	}

	// the space after
	offsetY = offsetY + 70

}

func MakePDF(warband Warband, multiPage bool) {
	pdf := gofpdf.New("P", "mm", "A4", "")
    pdf.SetMargins(0,0,0)
	pdf.SetTextColor(text_color_r, text_color_g, text_color_b)

	MakeStatisticPage(warband, pdf)
	MakeHeroPage(warband, pdf, multiPage)
	MakeHenchmenPage(warband, pdf, multiPage)

	// TODO: Make output name variable or use name of the input file
	err := pdf.OutputFileAndClose("warband-roaster.pdf")

	if err != nil {
		panic(err)
	}
}
