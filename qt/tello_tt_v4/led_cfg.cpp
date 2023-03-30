#include "led_cfg.h"
#include "QPalette"
//#include "QDebug"

led_cfg::led_cfg(QWidget *parent):QPushButton(parent)
{
    //按键一次按下，两次弹起
    setCheckable(true);
    //设置默认背景色
    setStyleSheet("background-color:rgb(238,238,238);");
    //初始化地址
    this->key_t = &rbg_choose;
    this->tello_led = &tello_cfg_set[0];
    this->key_t->key_color_set = No_Color;
}
void led_cfg::mousePressEvent(QMouseEvent * ev)
{
    if(ev->button()==Qt::LeftButton)
    {

        if(this->key_id<=LED_NUM)
        {
            /*两次按下不同结果*/
            if(this->key_count==0)
            {
                this->key_t->key_color_set = this->key_t->key_color_change;
                this->key_count=1;
            }
            else {
                this->key_t->key_color_set = No_Color;
                this->key_count = 0;
            }
            switch (this->key_t->key_color_set)
            {
                case No_Color:{
                    tello_led[this->key_id-1] = '0';
                    setStyleSheet("background-color:rgb(238, 238, 238);");
                }break;
                case R_Color:{
                      tello_led[this->key_id-1] = 'r';
                      setStyleSheet("background-color:rgb(255, 0, 0);");
                }break;
                case G_Color:{
                      tello_led[this->key_id-1] = 'p';
                      setStyleSheet("background-color:rgb(138,43,226);");
                }break;
                case B_Color:{
                    tello_led[this->key_id-1] = 'b';
                    setStyleSheet("background-color:rgb(0, 0, 255);");
                }break;
            }
        }
        else {
            switch (this->key_id)
            {
                case R_C:this->key_t->key_color_change =R_Color;break;
                case P_C:this->key_t->key_color_change =G_Color;break;
                case B_C:this->key_t->key_color_change =B_Color;break;
            }
            QPushButton::mousePressEvent(ev);//事件继续往下传递，否则信号和槽无效
        }
    }

}

void led_cfg::set_id(uint16_t key_id_t)
{
    this->key_id = key_id_t;
    if(this->key_id<= LED_NUM)
    {
        //按键一次按下，两次弹起
        setCheckable(true);
        //设置默认背景色
        setStyleSheet("background-color:rgb(238, 238, 238);");
    }
    else
    {
        setCheckable(false);
        this->rgb_border_show();
        if(this->key_id>B_C){setStyleSheet("background-color:rgb(238, 238, 238);");}
    }
    //测试按键标号是否正确
    //this->setText(QString::number(key_id_t));
}

/*根据选定颜色更新R、P、B待选框颜色*/
void led_cfg::rgb_border_show(void)
{
   /*R、P、B颜色选定状态、加入id判断、避免错误调用*/
    switch (this->key_t->key_color_change)
    {
        case No_Color:break;
        case R_Color:{
            switch (this->key_id)
            {
                case R_C:setStyleSheet("background-color:rgb(255, 0, 0);border:2px solid rgb(0,229,238);");break;
                case P_C:setStyleSheet("background-color:rgb(138,43,226);border:none");break;
                case B_C:setStyleSheet("background-color:rgb(0, 0, 255);border:none;");break;
            }
        }break;
        case G_Color:
        {
            switch (this->key_id)
            {
                case R_C:setStyleSheet("background-color:rgb(255, 0, 0);border:none;");break;
                case P_C:setStyleSheet("background-color:rgb(138,43,226);border:2px solid rgb(0,229,238);");break;
                case B_C:setStyleSheet("background-color:rgb(0, 0, 255);border:none;");break;
            }
        }break;
         case B_Color:{
            switch (this->key_id)
            {
                case R_C:setStyleSheet("background-color:rgb(255, 0, 0);border:none;");break;
                case P_C:setStyleSheet("background-color:rgb(138,43,226);border:none;");break;
                case B_C:setStyleSheet("background-color:rgb(0, 0, 255);border:2px solid rgb(0,229,238);");break;
            }
         }break;
    }
//    qDebug()<<this->key_id<<"key_t.key_color_change"<<this->key_t->key_color_change;
}

/*点阵中此led的状态*/
void led_cfg::reset(void)
{

    setCheckable(false);
    this->key_count = 0;
    tello_led[this->key_id-1] = '0';
    setStyleSheet("background-color:rgb(238, 238, 238);");
    setCheckable(true);
}
