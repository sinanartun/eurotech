import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 1000 },
    { duration: '1m', target: 1000 },
    { duration: '30s', target: 2000 },
    { duration: '1m', target: 2000 },
    { duration: '30s', target: 0 },
  ],
};

export default function () {
  const url = 'https://jh4l0dq6r8.execute-api.eu-north-1.amazonaws.com/default/ProcessEstateData';
  
  const payload = JSON.stringify({
    // Add relevant payload data here
    exampleKey: 'exampleValue'
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const response = http.post(url, payload, params);

  check(response, {
    'status is 200': (r) => r.status === 200,
    'response time is < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1); // simulate a user pause
}
