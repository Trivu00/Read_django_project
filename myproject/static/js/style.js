/** 
 * trong js có dấu ; hay không cũng được
 * tuy nhiên khi viết nhiều lệnh trong 1 dòng thì phải có dấu ; để ngăn cách
 */

/* Fact
a = 3;
a++ + --a != --a + a++  --> true

console.log('a' && 'b' && 'c') --> 'c'
console.log('a' || 'b' || null || 'd') --> 'a'

Backslash
console.log('\\') --> \

Template string
var a='Hello'
var b='world'
console.log(`${a} ${b}`)

console.log(NaN == NaN) --> false
*/

//khai báo biến
var fullName = "Nguyễn Huỳnh Bá Phúc";

/** 
 * cmt có dấu * mối dòng
 */

//cmt 1 dòng

/* cmt 1 khối */

/** Một số hàm Built-in
 *      alert : bật ra hộp thoại chỉ có thông báo
 *      console : hiển thị thông báo trong tab console
 *      confirm : giống alert và có thêm nút cancel
 *      prompt : giống confirm và có thêm ô nhập liệu
 *      setTimeout : chạy 1 hàm sau 1 khoảng millisecond
 *      setInterval : chạy 1 hàm sau mỗi khoảng millisecond
 */
/* Cách dùng Built-in
alert('alert');
console.log('console');
confirm('confirm');
prompt('prompt');
setTimeout(function () {
    console.log('st');
}, 10000);
setInterval(function () {
    console.log('st');
}, 10000);
 */

/* Các loại toán tử
Toán tử số học - Arithmetic
    +   -   *   **  /   %   ++  -- 
Toán tử gán - Assignment
    =   +=  -=  *=  /=  %=  <<=  >>=  >>>=  &=  ^=  |=  **=
Toán tử so sánh - Comparison
    ==  ===  !=  !==  >  <  >=  <=
Toán tử logic - Logical
    &&  ||  !
 */

/* Kiểu dữ liệu
Number
    var a = 1;
String
    var fullName = 'Nguyễn Phúc;
Boolean
    var isSuccess = true;
Undefined
    var a;
Null
    var isNull = Null;
Symbol
    var id1 = Symbol();
    var id2 = Symbol('id');
Function
    var myFunction = function() {
        alert("Hi")
    }
Object
    var myObject = {
        name: 'Phuc',
        birth: 2001
    }
Array
    var myArray = {
        'Javascript',
        123
    }
 */

/**Javascript keyword
 * Javascript string methods
 * Javascript array methods
 * Ternary operator
 */