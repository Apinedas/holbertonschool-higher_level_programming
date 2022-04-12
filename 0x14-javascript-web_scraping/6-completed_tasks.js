#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const completedTasks = {};

request(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const obtained = JSON.parse(body);
    for (const entry of obtained) {
      if (entry.completed) {
        const userId = entry.userId;
        if (Object.keys(completedTasks).includes(String(userId))) {
          completedTasks[userId] += 1;
        } else {
          completedTasks[userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
