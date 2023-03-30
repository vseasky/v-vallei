#ifndef CONFIG_H
#define CONFIG_H

#define LED_NUM 64
#define R_C 65
#define P_C 66
#define B_C 67

typedef enum {
No_Color = 0,
R_Color,
G_Color,
B_Color
}key_color;
class config
{
public:
    config();
    key_color key_color_set;
    key_color key_color_change;
};
extern config rbg_choose;
extern char tello_cfg_set[65];
#endif // CONFIG_H
