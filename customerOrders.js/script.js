
// Users and Orders in a Shopping App

//STEPS:
// Create classes with methods: Users (placeOrder, listOrders) and Orders (showOrder)
// Use classes
// Test Objects and methods


class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
        this.orders = [];
    }

    placeOrder(order) {
        this.orders.push(order);
        console.log(`${this.name} placed an order for ${order.itemName}`);
    }

    listOrders() {
        console.log(`Orders for ${this.name}: `);
        this.orders.forEach((order, index) => {
            console.log(`${index + 1}.${order.itemName} : ${order.price} Euro`);
        });
    }
}
class Order {
    constructor(itemName, price) {
        this.itemName = itemName;
        this.price = price;
        this.timestamp = new Date();
    }

    showOrder() {
        return `${this.itemName} -- ${this.price} Euro -- ordered on : ${this.timestamp.toLocaleString()}`
    }
}
const user1 = new User("Jane Doe", "janedoe@xml.com");
const user2 = new User("John Doe", "johndoe@google.com");
const order1 = new Order("Sword", 200);
const order2 = new Order("Book", 87);

user1.placeOrder(order2);
user2.placeOrder(order1);
user1.listOrders();
user2.listOrders();

console.log("Order Summary: ", order1.showOrder(), order2.showOrder());











