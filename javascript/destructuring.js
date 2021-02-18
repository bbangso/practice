// 비구조화

const student = {
    name: 'bbangso',
    course: 'ssafy 3rd',
    email: 'gmail@gmail.com',
    phone: '010123456789',
}

// const name = student.name
// const course = student.course
// const email = student.email
// const phone = student.phone

// // 일일이 할당하는것이 불편하다
// // 비구조화 => Object, array를 해체 

// const {name} = student
// const {course} = student
// const {email} = student
// const {phone} = student

// console.log(name, course, email, phone)

const { name, course, email, phone } = student
console.log(name, course, email, phone)      // key와 변수명이 같아야 한다. 순서를 바꿔도 된다

// 실전
function getStudentInfo(student){
    console.log(`Hi my name is ${student.name}, email is ${student.email}`)
}

function getStudentInfo2({name, email}) {
    console.log(`Hi my name is ${name}, email is ${email}`)
}


getStudentInfo(student)
getStudentInfo2(student)