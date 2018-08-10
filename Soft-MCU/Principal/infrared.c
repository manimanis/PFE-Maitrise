#include "infrared.h"

void ir_init() {
   output_high(IR_RQ_SEND);
}

int ir_is_data_ready() {
   return input(IR_DATA_READY);
}

int ir_get_data() {
   int c;
   
   if (input(IR_DATA_READY)) {
      DISABLE_INT;
      output_low(IR_RQ_SEND);
      c = fgetc(ir);
      output_high(IR_RQ_SEND);
      ENABLE_INT;
      return c;
   }
   
   return 0xff;
}
