# SudokuSolver

## Hedef

Kullanıcının girdiği değerleri alıp bu sudokunun çözümünü yapmak.

## Özet

1. Kullanıcıdan alınan değerlerin int dir değer olup olmadığını kontrol edelim.
2. Bu değerleri alıp matrix oluşturalım. 
3. Oluşturulan matrixin geçerli olup olmadığını test edelim.
4. Çözümünü yapıp tekrar ekrana verelim.

## Gereksinimler
Bu programı çalıştırabilmek için **Pyqt5** paketine ihtiyacımız var. Bu pakete komut satırınıza
<br/>
``pip install PyQt5`` yazarak sahip olabilirsiniz.
<br/><br/>
Ya da bu klasoru bilgisayarınıza indirip komut satırını bu klasorde açıp
<br/>
``pip install - r requirements.txt``
yazarak da bu pakete sahip olabilirsiniz.
<br/>
<br/>

## Programdan Görüntüler
Programı açtığımızda bizi böyle bir görüntü bekliyor olacak: 
<br/><br/>
![1.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/1.png)
<br/><br/>
Eğer biz direkt **SOLVE!** butonuna tıklarsak bizim matrix değerlerimizin hepsini 0 olarak algılayıp sudokuyu çözecektir.
<br/><br/>
![2.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/2.png)
<br/><br/>
Bunun yanında gerçek bir sudokunun çözümünü gösterelim:
<br/><br/>
![3.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/3.png)
<br/><br/><br/>
Bu sudoku değerlerini girip **SOLVE!** butonuna tıkladığımızda bize cevabı oluşturup ekranda verecektir:
<br/><br/>
![4.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/4.png)
<br/><br/><br/>
Peki **RESET** butonu ne işe yarıyor :<br/> 
**RESET** butonu da isminden anlayacağınız üzere ekranda yazan tüm değerleri silip programın ilk açıldığı andaki görüntüsünü almasını sağlıyor.
<br/><br/>
![1.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/1.png)
<br/><br/><br/>
Şimdi ise hatalı bir değer yani sonucu olmayan bir sudoku girelim : 
<br/><br/>
![5.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/5.png)
<br/> <br/>
Bu ekrandayken **SOLVE!** tuşuna basalım : 
<br/><br/>
![6.png](https://github.com/deveneskaracabay/SudokuSolver/blob/master/Images/6.png)
<br/><br/>
Göründüğü üzere bizim geçersiz değerler girdiğimizi söyleyecektir.
<br/><br/>
#### Programın bir üst versiyonuna [buradan](https://github.com/deveneskaracabay/Sudoku-Solver-With-Images) ulaşabilirsiniz.
