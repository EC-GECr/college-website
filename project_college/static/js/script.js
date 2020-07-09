// Handling Registration data

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
    // Board10 = form2.board1.value;
    TenthRoll = form2.tenthroll.value;
    TenthCent = form2.tenthcent.value;

    // Board12 = form2.board2.value;
    TwelthRoll = form2.twelthroll.value;
    TwelthCent = form2.twelthcent.value;

    PETRoll = form2.petroll.value;
    PETCent = form2.petrank.value;
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

    form4.submit();
});
