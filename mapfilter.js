// // map and filter in javascript
// const array1 = [1, 4, 9, 16];

// // Pass a function to map
// //const map1 = array1.map((x) => x * 2);
// const map1 = array1.filter((x) => x * 2);

// console.log(map1);
// // Expected output: Array [2, 8, 18, 32]

const numbers = [1, 2, 3, 4];
const filteredNumbers = numbers.map((num, index) => {
  if (index < 3) {
    console.log(num);
  }
});


// index goes from 0, so the filterNumbers are 1,2,3 and undefined.
// filteredNumbers is [1, 2, 3, undefined]
// numbers is still [1, 2, 3, 4]