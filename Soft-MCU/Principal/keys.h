#ifndef __KEYS_H__

#define __KEYS_H__

#define KEY_ONOFF 'A'
#define KEY_MUTE  'B'
#define KEY_EPG   'C'
#define KEY_DOTS  'D'
#define KEY_INFO  'E'
#define KEY_0     '0'
#define KEY_1     '1'
#define KEY_2     '2'
#define KEY_3     '3'
#define KEY_4     '4'
#define KEY_5     '5'
#define KEY_6     '6'
#define KEY_7     '7'
#define KEY_8     '8'
#define KEY_9     '9'
#define KEY_EXIT  'G'
#define KEY_UP    'H'
#define KEY_DOWN  'K'
#define KEY_LEFT  'I'
#define KEY_RIGHT 'J'
#define KEY_OK    'L'
#define KEY_NPRG  'M'
#define KEY_PPRG  'N'
#define KEY_RCL   'O'
#define KEY_TVRDO 'P'
#define KEY_FAV   'Q'
#define KEY_LANG  'R'
#define KEY_BLUE  'S'
#define KEY_WHITE 'T'
#define KEY_MENU  'F'

#define MENU_PRAYER_CALLER          0
#define MENU_CONFIG_MP3             1
#define MENU_CONFIG_HOURS           2
#define MENU_CONFIG_DATE            3
#define MENU_CONFIG_TOWN            4
#define MENU_CONFIG_PRAYERS         5

#define MENU_COUNT                  6

#define MENU_CONFIG_HOURS_HOURS     1
#define MENU_CONFIG_HOURS_MINUTES   2

#define MENU_CONFIG_DATE_DAY        1
#define MENU_CONFIG_DATE_MONTH      2
#define MENU_CONFIG_DATE_YEAR       3

#define MENU_CONFIG_PRAYERS_TIMES1  1
#define MENU_CONFIG_PRAYERS_TIMES2  2
#define MENU_CONFIG_PRAYERS_FAJR    3
#define MENU_CONFIG_PRAYERS_SHURUQ  4
#define MENU_CONFIG_PRAYERS_THUHR   5
#define MENU_CONFIG_PRAYERS_ASR     6
#define MENU_CONFIG_PRAYERS_MAGHREB 7
#define MENU_CONFIG_PRAYERS_ISHAA   8

#define MENU_CONFIG_TOWN_NUMBER     0

#define MENU_CONFIG_MP3_PLAY        1
#define MENU_CONFIG_MP3_STOP        2

#define USER_TIME_CHANGED           1
#define USER_DATE_CHANGED           2
#define USER_TOWN_CHANGED           3
#define USER_PRAYERS_CHANGED        4
#define USER_POWERON_CHANGED        5
#define USER_PLAY_SOUND             6
#define USER_STOP_SOUND             7

void show_menu();
int handle_key(int key);


#endif // __KEYS_H__
