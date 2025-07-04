let array =[ -14, 4, 5, -2, 76]
let array2 = [] 
let check_value = 0 

for (let i=0; i<array.length;i++){
    check_value = array[i]

    if ( check_value <=0 ){
        continue
    }
    else if (check_value>0){
        array2[array2.length]= check_value
    }
}
console.log("Positive Numbers are: ", array2) //output
