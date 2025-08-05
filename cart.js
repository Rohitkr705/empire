var product_total_amount=document.getElementById('product_total_amount');
var shipping_charge=document.getElementById('shipping_charge');
var total_cart_amt=document.getElementById('total_cart_amt');
var discountCode=document.getElementById('discount_code1');

const decreasenumber = (incdec,itemprice) => {
    var itemval=document.getElementById(incdec);
    var itemprice=document.getElementById(itemprice);

    if(itemval.value<=0){
        itemval.value=0;
        alert('Negative quantity not allowed');
    }else{
        itemval.value=parseInt(itemval.value)-1;
        itemval.style.background='#fff';
        itemval.style.color='#000';
        itemprice.innerHTML=parseInt(itemprice.innerHTML)-100;
        product_total_amount.innerHTML=parseInt(product_total_amount.innerHTML)-100;
        total_cart_amt.innerHTML=parseInt(product_total_amount.innerHTML)+parseInt(shipping_charge.innerHTML);
        }
}

const increasenumber = (incdec,itemprice) => {
    var itemval=document.getElementById(incdec);
    var itemprice=document.getElementById(itemprice);
    if(itemval.value>=5){
        itemval.value=5;
        alert('max 5 allowed');
        itemval.style.background='red';
        itemval.style.color='#fff';
    }else{
        itemval.value=parseInt(itemval.value)+1;
        itemprice.innerHTML=parseInt(itemprice.innerHTML)+100;
        product_total_amount.innerHTML=parseInt(product_total_amount.innerHTML)+100;
        total_cart_amt.innerHTML=parseInt(product_total_amount.innerHTML)+parseInt(shipping_charge.innerHTML);
        }
}

const discount_code= () => {
    let totalamtcurr=parseInt(total_cart_amt.innerHTML);
    let error_trw=document.getElementById('error_trw');
    if(discountCode.value === 'MCA'){
        if(totalamtcurr > 50)
        {
        let newtotalamt=totalamtcurr-100;
        total_cart_amt.innerHTML=newtotalamt;
        error_trw.innerHTML="Hurry! code is valid";
        }
        else{
           alert("Add a book to apply discount");
        }
    }
    else{
        error_trw.innerHTML="Try again valid code is MCA";
    }
}

