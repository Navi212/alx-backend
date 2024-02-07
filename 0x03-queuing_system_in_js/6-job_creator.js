/*
Create the Job creator
*/
import { createClient } from "redis";
const kue = require("kue");
const queue = kue.createQueue();
const jobData = {phoneNumber: "+23423xxxxxx", message: "My dummy telephone line",};
const client = createClient();
client
.on("connect", () => console.log("Redis client connected to the server"))
.on("error", err => console.log(`Redis client not connected to the server: ${err}`));
const job = queue.create("push_notification_code", jobData)
.save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});
job
.on("complete", () => console.log("Notification job completed"))
.on("failed", () => console.log("Notification job failed"));
