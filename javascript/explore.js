let TWILIO_AUTH_SID;
let TWILO_AUTH_TOKEN;
const Twilio = require("twilio");

const client = new Twilio(
  "AC2a7c23dc33b299ebd312a453c9adb7b8",
  "bc4ff5f356d4a11a1f18c88d0801b78d"
);

client.messages
  .list()
  .then((messages) =>
    console.log(`The most recent message is ${messages[0].body}`)
  ).catch((err) =>console.error(err));

console.log("Gathering your messages.....");
