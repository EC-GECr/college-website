setTimeout(function () {
    $('#message').fadeOut('slow');
}, 3500);

// Handling Registration data

//
// $(document).ready(function() {
//
//     $('#submit').attr('disabled', true);
//     $('#id_new_password1').on('keyup', validatePassword);
//
//     $('input').on('keyup', validateSubmit);
//
//     function validatePassword() {
//         var val = $('#id_new_password1').val();
//         var flag = true;
//
//         if (val === '') {
//             $('#password-status').text("Password can't be blank.");
//         } else if (/\s/.test(val)) {
//             $('#password-status').text("Password can't contain whitespace.");
//         } else if (!/\d/.test(val)) {
//             $('#password-status').text("Password must contain at least one digit.");
//         } else if (!/[A-Z]/.test(val)) {
//             $('#password-status').text("Password must contain at least one uppercase letter.");
//         } else if (val.length < 6 || val.length > 15) {
//             $('#password-status').text("Password length must be between 6 and 15 characters.");
//         } else {
//             flag = false;
//         }
//
//         if (flag) {
//             $('#password-status').addClass('invalid');
//         } else {
//             $('#password-status').removeClass('invalid').text("OK");
//         }
//     }
//
//     function validateSubmit() {
//         $('#submit').attr('disabled', ( $('.invalid').length > 0) );
//     }
// });

let allAreFilled = true;
// form-1
const form1 = document.getElementById('form-1');
let firstName, lastName, Email, Phone, Roll, Enroll;
const btn1 = document.getElementById('btn-1');

btn1.addEventListener('click', (e) => {

    firstName = form1.firstname.value;
    lastName = form1.lastname.value;
    Email = form1.email.value;
    Phone = form1.phone.value;
    Roll = form1.roll.value;
    Enroll = form1.enroll.value;
});

// form-2
const form2 = document.getElementById('form-2');
let Board10, TenthRoll, TenthCent, Board12, TwelthRoll, TwelthCent, PETRoll, PETRank;
const btn2 = document.getElementById('btn-2');

btn2.addEventListener('click', (e) => {
    Board10 = document.querySelector("#board1").value;

    TenthRoll = form2.tenthroll.value;
    TenthCent = form2.tenthcent.value;

    Board12 = document.querySelector("#board2").value;
    TwelthRoll = form2.twelthroll.value;
    TwelthCent = form2.twelthcent.value;

    PETRoll = form2.petroll.value;
    PETRank = form2.petrank.value;
    // console.log(Board10, Board12, TenthCent, TenthRoll)
    // console.log(form2);
});

// form-3
const form3 = document.getElementById('form-3');
let FatherFirst, FatherLast, FatherJob, FatherPhone, MotherFirst, MotherLast, MotherJob, MotherPhone;
const btn3 = document.getElementById('btn-3');

btn3.addEventListener('click', (e) => {
    FatherFirst = form3.fatherfirst.value;
    FatherLast = form3.fatherlast.value;
    FatherJob = form3.fatherjob.value;
    FatherPhone = form3.fatherphone.value;

    MotherFirst = form3.motherfirst.value;
    MotherLast = form3.motherlast.value;
    MotherJob = form3.motherjob.value;
    MotherPhone = form3.motherphone.value;
});

// form-4: basic-info
const form4 = document.getElementById('basic-info');
const btn4 = document.getElementById('btn-4');

btn4.addEventListener('click', (e) => {
    // e.preventDefault();

    form4.firstName.value = firstName;
    form4.lastName.value = lastName;
    form4.Email.value = Email;
    form4.Phone.value = Phone;
    form4.Roll.value = Roll;
    form4.Enroll.value = Enroll;

    form4.Board10.value = Board10;
    form4.TenthRoll.value = TenthRoll;
    form4.TenthCent.value = TenthCent;
    form4.Board12.value = Board12;
    form4.TwelthRoll.value = TwelthRoll;
    form4.TwelthCent.value = TwelthCent;
    form4.PETRoll.value = PETRoll;
    form4.PETRank.value = PETRank;

    form4.FatherFirst.value = FatherFirst;
    form4.FatherLast.value = FatherLast;
    form4.FatherJob.value = FatherJob;
    form4.FatherPhone.value = FatherPhone;
    form4.MotherFirst.value = MotherFirst;
    form4.MotherLast.value = MotherLast;
    form4.MotherJob.value = MotherJob;
    form4.MotherPhone.value = MotherPhone;

    form4.submit();
});

