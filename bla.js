function whoIsGoingHomeEarly(n, k) {
  const workersGoingHome = [];
  const remainingWorkers = Array.from(Array(n), (_, index) => index + 1);
  const half = Math.ceil(n / 2);
  let currSize = n;
  let startingIndex = 0;

  while (currSize > half) {
    const workerIndex = (startingIndex + k) % currSize;
    workersGoingHome.push(remainingWorkers[workerIndex]);
    remaining.splice(workerIndex, 1);
    currSize--;
    startingIndex = workerIndex % currSize;
  }

  return workersGoingHome;
}
