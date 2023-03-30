#ifndef LED_CFG_H
#define LED_CFG_H


#include "config.h"
#include <QPushButton>
#include <QMouseEvent>



class led_cfg : public QPushButton
{
public:
    led_cfg(QWidget *parent=0);
    void set_id(uint16_t key_id_t);
    void set_color_change(key_color *color_t);
    void rgb_border_show(void);
    void reset(void);
    char * tello_led;
private:
    uint16_t key_id;
    uint8_t key_count;
    config *key_t;
protected:
    void mousePressEvent(QMouseEvent * ev);
};

#endif // CMYPUSHBUTTON_H
