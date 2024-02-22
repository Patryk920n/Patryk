<?php
//zad20
class car{
    public $marka;
    public $model;
    public $rok;

    function __construct($marka, $model, $rok){
        $this->marka = $marka;
        $this->model = $model;
        $this->rok = $rok;
    }

    public function getMarka()
    {
        return $this->marka;
    }
    function toString()
    {

        return"Marka: $this->marka model: $this->model rok: $this->rok";
    }
}
//zad 19
    class algorithm{
        function palindromem($word)
        {
            $pali = str_split($word,1);

        }
}


//zad1
//echo date("d-m-Y-H-i-s");
//zad 2
//echo "Podaj imię";
//$imie = fgets(STDIN);
//echo $imie;
//zad3
//echo "Podaj liczbe";
//$l1 = fgets(STDIN);
//$l2 = fgetc(STDIN);
//echo $l2+$l1;

//zad20
$car1 = new car("aa","bb","20.12.2020");
echo $car1->toString();
//$car1->String();