init python:
    player_pts = 0
    opp_pts = 0

init python:
    style.big_text.font = "fonts/DK Prince Frog.otf"
    style.big_text.size = 40
    #  style.big_text = Style(style.default)
    #  style.big_text.size = 42

screen score():
    frame:
        background Solid("#00000078") #Null()
        align (0.01, 0.03)
        has vbox
        text "HP : [hp_pts]" style "big_text"
        text "Level : [opp_pts]" style "big_text"
        text "EXP : [exp_pts]" style "big_text"

screen health_bar:
    vbox:
        xalign 0.2 yalign 0.03
        bar value AnimatedValue(health, range=100.0):
            xalign 0.0 yalign 0.0
            xmaximum 200 # ukuran bar health
            ymaximum 30
            left_bar Frame("images/bar_health_ful.png", 10, 0)
            right_bar Frame("images/bar_health_kosong.png", 10, 0)
            thumb None
            # bar_vertical True
        # image ConditionSwitch(
        #     "health <=0", "images/bar_heath_icon_death.png",
        #     "health >=1", "images/bar_heath_icon.png",
        # )

