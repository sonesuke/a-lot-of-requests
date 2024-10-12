import http from 'k6/http';
import { sleep } from 'k6';
export const options = {
  vus: 10,
  duration: '10s',
};
export default function () {
  http.get('http://web:8080/django/workload/prime-number');
}