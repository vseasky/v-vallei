#include "config.h"
config rbg_choose;
char tello_cfg_set[65];
config::config()
{
    /*设置初始值*/
    for(int i=0;i<LED_NUM;i++)
    {
        tello_cfg_set[i]='0';
    }
    tello_cfg_set[LED_NUM]='\0';
    this->key_color_set = No_Color;
    this->key_color_change =R_Color;
}
