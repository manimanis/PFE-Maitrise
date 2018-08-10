#include <16F628A.h>

#FUSES NOWDT                    //No Watch Dog Timer
#FUSES NOMCLR                   //Master Clear pin used for I/O
#FUSES NOBROWNOUT               //No brownout reset
#FUSES NOLVP                    //No low voltage prgming, B3(PIC16) or B5(PIC18) used for I/O

#define DATA PIN_B5
#define STB  PIN_B6
#define CLK  PIN_B7

#define DOTS_IN PIN_A3

#define IN1 PIN_B0
#define IN2 PIN_B1
#define IN3 PIN_B2
#define IN4 PIN_B3

#use delay(crystal=20000000)
#use i2c(master,sda=PIN_A2,scl=PIN_A1,SLOW)

