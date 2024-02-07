/*
Connect to node_redis
*/
import { createClient, print } from "redis";
const util = require("util");
const client = createClient();
client
.on("connect", () => console.log('Redis client connected to the server'))
.on("error", err => console.log(`Redis client not connected to the server: ${err}`));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

const asyncRetVal = util.promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try{
        const data = await asyncRetVal(schoolName);
        console.log(`${data}`);
    }
    catch(err){
        console.log(`${err}`);
    }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
