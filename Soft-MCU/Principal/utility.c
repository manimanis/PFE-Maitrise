#include <utility.h>

int bcd2dec(int val) {
   return (val >> 4) * 10 + (val & 0x0f);
}

int dec2bcd(int val) {
   return ((val / 10) << 4) + (val % 10);   
}
