/*
Redis subscriber
*/
import { createClient } from "redis";
const client = createClient();
const channel = "holberton school channel";
const command = "KILL_SERVER";
client
.on("connect", () => console.log("Redis client connected to the server"))
.on("error", err => console.log(`Redis client not connected to the server: ${err}`));
client.subscribe(channel);
client
.on("message", (_channel, message) => {
    if (message === command) {
        client.unsubscribe();
        client.quit();
    }
    console.log(message);
});