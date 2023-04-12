(* 1 *)
not (true && false) ;;

(* 2 *)
float_of_int(int_of_float(5.0))


(* 3 *)
float_of_int(int_of_float (sin (3.14 /. 2.0 ** 2.0) +. cos (3.14 /. 2.0 ** 2.0)))


(* 4 *)
int_of_float(sqrt(float_of_int(3*3 + 4*4)))



(* 以下、出力結果 *)

(* 1 *)
not (true && false) ;;
- : bool = true


(* 2 *)
float_of_int(int_of_float(5.0)) ;;
- : float = 5.



(* 3 *)
float_of_int(int_of_float (sin (3.14 /. 2.0 ** 2.0) +. cos (3.14 /. 2.0 ** 2.0))) ;;
- : float = 1.


(* 4 *)
int_of_float(sqrt(float_of_int(3*3 + 4*4))) ;;
- : int = 5
