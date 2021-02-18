const name = 'bbang'
const obj1 = {
    name: name,
    sayHello: function () {
        return `Hi my name is ${this.name}`
    }
}

// 같은 표현 (ES6)

const obj2 = {
    name,
    sayHello () {
        return `Hi my name is ${this.name}`
    }
}

console.log(obj1, obj2)

