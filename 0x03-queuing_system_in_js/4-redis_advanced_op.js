/*
Store a hash value
*/
import { createClient, print } from "redis";
const client = createClient();
client
.on("connect", () => console.log('Redis client connected to the server'))
.on("error", err => console.log(`Redis client not connected to the server: ${err}`));

client.hset("HolbertonSchools", "Portland", "50", print);
client.hset("HolbertonSchools", "Seattle", "80", print);
client.hset("HolbertonSchools", "New York", "0", print);
client.hset("HolbertonSchools", "Bogota", "20", print);
client.hset("HolbertonSchools", "Cali", "40", print);
client.hset("HolbertonSchools", "Paris", "2", print);

client.hgetall("HolbertonSchools", (err, result) => {
    if (err) {
        console.log(err);
        throw new Error(err);
    }
    console.log(result);
});