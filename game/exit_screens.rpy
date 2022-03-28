## Screen with Stats Button
# default knowledge = 1
# default charm = 2
# default guts = 3
# default kindness = 4
# default proficiency = 5

screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        # xoffset -30 batas margin
        # yoffset 30
        idle "UI/button_idle.png"
        hover "UI/button_hover.png"
        # action ShowMenu("StatsUI")
        action Quit(confirm=not main_menu)
        # action Quit(confirm=not main_menu)
        
# # Stats UI
# screen StatsUI:
#     add "UI/bg peach.png"
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xpadding 30
#         ypadding 30

#         hbox:
#             style_prefix "slider"
#             box_wrap True
            

#             vbox:
#                     text "Pause Menu" size 40
#                     if config.has_music:
#                         label _("Volume Musik")

#                         hbox:
#                             bar value Preference("music volume")
                            
#                     if config.has_sound:

#                         label _("Kecepatan Text")

#                         hbox:
#                             bar value Preference("text speed")

#                     imagebutton:
#                         xalign 0.5
#                         yalign 0.0
#                         xoffset -30
#                         yoffset 30
#                         auto "UI/kembali_%s.png"
#                         action Return()
                    
#                     imagebutton:
#                         xalign 0.5
#                         yalign 0.0
#                         xoffset -30
#                         yoffset 50
#                         auto "UI/keluar_%s.png"
#                         action Quit(confirm=not main_menu)
                        



        



            # Text Column
            # vbox:
            #     spacing 10
            #     text "Pause Menu" size 40
            #     text "Charm" size 40
            #     text "Guts" size 40
            #     text "Kindness" size 40
            #     text "Proficiency" size 40

            # Values Column     
            # vbox:    
            #     spacing 10
            #     # text "[knowledge]" size 40
            #     if config.has_music:
            #             label _("Volume Musik")

            #             hbox:
            #                 bar value Preference("music volume")

            #     text "[charm]" size 40
            #     text "[guts]" size 40
            #     text "[kindness]" size 40
            #     text "[proficiency]" size 40
    
    ## Show a Return button
    # imagebutton:
    #     xalign 1.0
    #     yalign 0.0
    #     xoffset -30
    #     yoffset 30
    #     auto "UI/return_%s.png"
    #     action Return()
