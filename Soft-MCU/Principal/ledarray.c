#include "ledarray.h"

void ldarr_show(int sel, int val) {
   if (sel == 0) {
      putc(val, ld1);
   } else {
      putc(val, ld2);
   }
}

void ldarr_off(int sel) {
   if (sel == 0) {
      putc(0, ld1);
   } else {
      putc(0, ld2);
   }
}
