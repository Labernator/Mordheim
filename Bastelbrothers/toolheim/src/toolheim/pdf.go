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

	tr := pdf.UnicodeTranslatorFromDescriptor("")

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

        // paint border
        pdf.SetXY(5.5,float64(offsetY)+6)
        pdf.CellFormat(198, 39.25, "", "1", 0, "", false, 0, "")

		// Name
		pdf.SetFont("Arial", "B", 12)
		pdf.SetXY(6, float64(offsetY + 4))
		pdf.Write(11, tr(hero.Name))

		// Type
		pdf.SetFont("Arial", "", 12)
		pdf.SetXY(6, float64(offsetY + 10))
		pdf.Write(11, tr(hero.Type))

		// Stats
		pdf.SetFillColor(255, 0, 0)
		pdf.SetFont("Arial", "", 13)
		pdf.SetFontUnitSize(5)

		// skills stats
		pdf.SetXY(5, float64(offsetY + 32))
		pdf.Image("images/hero_skllist_stats.png", 5.5, -20, 1499*0.045, 295*0.045, true, "", 0, "")

		pdf.SetXY(6.5, float64(offsetY + 36))
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
		pdf.SetX(46.5)
		pdf.Write(11, strconv.Itoa(hero.Stats.Initiative))
		pdf.SetX(53)
		pdf.Write(11, strconv.Itoa(hero.Stats.Attacks))
		pdf.SetX(59.5)
		pdf.Write(11, strconv.Itoa(hero.Stats.Leadership))
		pdf.SetX(66.0)
		pdf.Write(11, hero.Stats.Save)

		// Skill lists
        pdf.SetY(float64(offsetY) + 33.83)
		if hero.bSkillLists.Combat == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetX(6.5)
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Shooting == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetX(17.75)
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Academic == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetX(28.72)
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Strength == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetX(40.5)
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Speed == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetX(51.5)
			pdf.Write(0, marker_sign)
		}
		if hero.bSkillLists.Special == true {
			pdf.SetFont("Arial", "B", 10)
			pdf.SetX(60.7)
			pdf.Write(0, marker_sign)
		}

        pdf.SetFont("Arial", "", 10)

		// Weapons
		pdf.SetXY(46, float64(offsetY + 14))
		pdf.Write(0, tr(hero.Weapons))

		// Armour
		pdf.SetFont("Arial", "", 10)
		pdf.SetXY(46, float64(offsetY + 18))
		pdf.Write(0, tr(hero.Armour))

		// Rules
		pdf.SetXY(46, float64(offsetY + 22))
		pdf.Write(0, tr(hero.Rules))

		if len(hero.Injuries) > 0 {
			pdf.SetFont("Arial", "", 10)
			pdf.SetXY(46, float64(offsetY + 26))
			pdf.Write(0, tr(hero.Injuries))
		}

		if hero.HiredSword {
			// show hired sword marker
			pdf.SetXY(0, float64(offsetY) + 18.5)
			pdf.Image("images/hiredsword_marker.png", 6, 0, 421*0.053, 97*0.053, true, "", 0, "")
		}

		if hero.DramatisPersonae {
			// show dramatis personae marker
			pdf.SetXY(0, float64(offsetY) + 18.5)
			pdf.Image("images/dp_marker.png", 6, 0, 421*0.053, 97*0.051, true, "", 0, "")
		}

		if hero.Large {
			// show large creature marker
			pdf.SetXY(0, float64(offsetY) + 18.5)
            if hero.HiredSword {
                pdf.Image("images/large.png", 29.5, 0, 421*0.03, 97*0.05, true, "", 0, "")
            } else {
                pdf.Image("images/large.png", 6, 0, 421*0.03, 97*0.05, true, "", 0, "")
            }
		}

		// Background
		pdf.SetXY(5.25, float64(offsetY) + 30.5)
		pdf.Image("images/hero_xp_bar.png", 73.0, 0, 1499*0.0695, 295*0.042, true, "", 0, "")

		// XP
		pdf.SetFont("Arial", "", 12)
		pdf.SetXY(180, float64(offsetY+30))
		pdf.Write(20, strconv.Itoa(hero.Experience) + " xp")
		y := 0.0
		reduce_x := 0
                space_x := 3.43
                tmp_off_y := 0.0
		for x := 1; x <= hero.Experience; x++ {
			xx := x
			if hero.SlowWitted == false {
			    pdf.SetFont("Arial", "B", 10)
			} else {
			    pdf.SetFont("Arial", "B", 6)
                            space_x = 3.43 / 2.0
                            tmp_off_y = -0.61
			}
			if reduce_x > 0 {
                                if hero.SlowWitted == false {
				    xx = xx - reduce_x*30
                                } else {
				    xx = xx - reduce_x*60
                                }
			}
			pdf.SetXY(float64(72.5+((float64(xx)-1.0)*space_x)), float64(offsetY) + float64(tmp_off_y) + float64(y) * 15.0 + 34.2)
			pdf.Write(0, marker_sign)
			if hero.SlowWitted == false && (x == 30 || x == 60) {
				y = y + 0.22
				reduce_x = reduce_x + 1
			} else if (hero.SlowWitted == true && (x == 60 || x == 120)) {
				y = y + 0.22
				reduce_x = reduce_x + 1
                        }
		}

	}

	offsetY = offsetY + shiftY

}

func MakeHenchmenPage(warband Warband, pdf *gofpdf.Fpdf, newPage bool) {

	tr := pdf.UnicodeTranslatorFromDescriptor("")

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

        // paint border
        pdf.SetXY(5.5,float64(offsetY)+6)
        pdf.CellFormat(198, 29.25, "", "1", 0, "", false, 0, "")

		pdf.SetFont("Arial", "B", 12)
		// Name
		pdf.SetY(float64(offsetY + 4))
		pdf.SetX(6)
		pdf.Write(11, tr(henchmen.Name))

		// Type
		pdf.SetFont("Arial", "", 12)
		pdf.SetY(float64(offsetY + 9))
		pdf.SetX(6)
		pdf.Write(11, tr(henchmen.Type))

		// Number
		pdf.SetFont("Arial", "", 12)
		pdf.SetY(float64(offsetY + 14))
		pdf.SetX(6)
		pdf.Write(11, "x" + strconv.Itoa(henchmen.Number))

		if henchmen.AttackAnimal && !henchmen.Mount  {
			// show attack animal marker, if the henchmen unit s a attack animal and a mount, only show the mount marker
			pdf.SetXY(0, float64(offsetY) + 17)
			pdf.Image("images/attackanimal.png", 15, 0, 421*0.033, 97*0.055, true, "", 0, "")
		}

		if henchmen.Mount {
			// show mount marker
			pdf.SetXY(0, float64(offsetY) + 17)
			pdf.Image("images/mount.png", 15, 0, 421*0.033, 97*0.055, true, "", 0, "")
		}

		if henchmen.Large {
			// show large creature marker
			pdf.SetXY(0, float64(offsetY) + 17)
            if henchmen.Mount {
                pdf.Image("images/large.png", 30, 0, 421*0.03, 97*0.050, true, "", 0, "")
            } else {
                pdf.Image("images/large.png", 15, 0, 421*0.03, 97*0.050, true, "", 0, "")
            }
		}

		// Stats
		// Background stats
		pdf.SetX(6)
		pdf.SetY(float64(offsetY) + 25.5)
		pdf.Image("images/henchmen_stats.png", 6, 0, 1499*0.044, 218*0.033, true, "", 0, "")

		pdf.SetFillColor(255, 0, 0)

		pdf.SetFont("Arial", "", 12)
		pdf.SetFontUnitSize(5)

		pdf.SetY(float64(offsetY) + 24.5)
		pdf.SetX(7.5)
		if len(henchmen.Stats.Movement) > 1 {
			pdf.SetX(3)
		}
		pdf.Write(11, henchmen.Stats.Movement)
		pdf.SetX(14)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.WeaponSkill))
		pdf.SetX(20.5)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.BallisticSkill))
		pdf.SetX(27.25)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Strength))
		pdf.SetX(33.5)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Toughness))
		pdf.SetX(40)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Wounds))
		pdf.SetX(46)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Initiative))
		pdf.SetX(53)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Attacks))
		pdf.SetX(59.0)
		pdf.Write(11, strconv.Itoa(henchmen.Stats.Leadership))
		if len(henchmen.Stats.Save) > 1 {
			pdf.SetX(63.7)
		} else {
			pdf.SetX(66.0)
		}
		pdf.Write(11, henchmen.Stats.Save)

		// Weapons
		pdf.SetFont("Arial", "", 10)
		pdf.SetXY(46, float64(offsetY + 14))
		pdf.Write(0, tr(henchmen.Weapons))

		// Armour
		pdf.SetFont("Arial", "", 10)
		pdf.SetXY(46, float64(offsetY + 18))
		pdf.Write(0, tr(henchmen.Armour))

		// Rules
		pdf.SetXY(46, float64(offsetY + 22))
		pdf.Write(0, tr(henchmen.Rules))

		// Background xp
		pdf.SetX(5)
		pdf.SetY(float64(offsetY) + 25.5)
		pdf.Image("images/henchmen_xp_bar.png", 75, 0, 1499*0.033, 218*0.033, true, "", 0, "")

		// XP
		pdf.SetFont("Arial", "", 12)
		pdf.SetXY(127, float64(offsetY + 21))
		pdf.Write(20, strconv.Itoa(henchmen.Experience) + " xp")
		for x := 1; x <= henchmen.Experience; x++ {
            pdf.SetFont("Arial", "B", 12)

            space_x := 3.45
            tmp_off_y := 0.0

            if henchmen.SlowWitted == true {
                space_x = space_x / 2.0
                tmp_off_y = 0.3
                pdf.SetFont("Arial", "B", 6)
            }

            pdf.SetXY(float64(74.6+((float64(x)-1.0)*space_x)), float64(offsetY) - float64(tmp_off_y) + 30.5)
            pdf.Write(0, marker_sign)
		}

	}

}

func MakeStatisticPage(warband Warband, pdf *gofpdf.Fpdf) {

	tr := pdf.UnicodeTranslatorFromDescriptor("")

	// Statistic page
	pdf.AddPage()

	startY = 23
	offsetY = 0

	// First page warband heading
	pdf.SetFont("Arial", "B", 28)
	pdf.SetXY(5, 5)
	pdf.Write(11, tr(warband.Warband.Name))
	pdf.SetFont("Arial", "B", 17)
	pdf.SetXY(5, 13)
	pdf.Write(11, tr(warband.Warband.Race))

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(5, 20)
	pdf.Write(10, "Alignment: " + tr(warband.Alignment))

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
			pdf.Write(11, tr(e))
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
	pdf.SetXY(72.5, float64(offsetY)+28.0)
	pdf.SetTextColor(0, 0, 0)
	pdf.Write(0, "Sell shard: ")
	pdf.SetFont("Arial", "", 10)
	pdf.SetTextColor(text_color_r, text_color_g, text_color_b)
	pdf.SetXY(93, float64(offsetY)+28.0)
	pdf.Write(0, strconv.Itoa(warband.member_cnt - warband.large_hiredsword_cnt - warband.dramatispersonae_cnt + warband.mount_cnt + warband.large_mount_cnt + warband.attackanimal_cnt ))

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
	pdf.Write(0, "( "+strconv.Itoa(warband.hiredsword_cnt + warband.large_hiredsword_cnt)+" )")
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55.0, float64(offsetY)+24.5)
	pdf.Write(0, strconv.Itoa(warband.hiredsword_sum_xp + warband.large_hiredsword_sum_xp) + " (+" + strconv.Itoa((warband.hiredsword_cnt) * 5) + ")")

	pdf.SetFont("Arial", "B", 10)
	pdf.SetXY(34.05, float64(offsetY)+28.0)
	pdf.Write(0, "( "+strconv.Itoa(warband.dramatispersonae_cnt)+" )")
	pdf.SetFont("Arial", "", 10)
	pdf.SetXY(55.0, float64(offsetY)+28.0)
	pdf.Write(0, strconv.Itoa(warband.dramatispersonae_sum_wbr))

	mount_aanim_s := ""
	if warband.attackanimal_cnt > 0 {
		mount_aanim_s = "Attack animals: (" + strconv.Itoa(warband.attackanimal_cnt) + ")   " + strconv.Itoa(warband.attackanimal_cnt * 10) + "   "
	}
	if warband.mount_cnt > 0 {
		mount_aanim_s = mount_aanim_s + "Mounts: (" + strconv.Itoa(warband.mount_cnt) + ")   " + strconv.Itoa(warband.mount_cnt * 10) + "   "
	}
	if warband.mount_cnt > 0 {
		mount_aanim_s = mount_aanim_s + "Large mounts: (" + strconv.Itoa(warband.large_mount_cnt) + ")   " + strconv.Itoa(warband.large_mount_cnt * 20) + "   "
	}
	if len(mount_aanim_s) > 1 {
		pdf.SetFont("Arial", "B", 10)
		pdf.SetXY(7.0, float64(offsetY)+36.25)
		pdf.Write(0, mount_aanim_s)
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
	pdf.Write(0, tr(warband.Objective))

	// achievments block 
	pdf.SetFont("Arial", "", 10)
	lines := pdf.SplitLines([]byte(warband.Achievments), 190)
	ox := 0
	oy := 0
	for i := 0; i < len(lines); i++ {
		pdf.SetXY(float64(7.0 + ox), float64(offsetY + 14 + i * 5) + float64(oy))
		pdf.Write(0, tr(string(lines[i])))
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
		pdf.Write(0, tr(string(lines[i])))
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

