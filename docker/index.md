---
abstract: A brief usage guide for the testing container build and run process.
authors:
  - name: Xander Harris
  - email: xandertheharris@gmail.com
date: 2025-10-26
title: Test container build
---

1. Build the thing.

   ```{code-block} shell
   docker build -t hr-test -f docker/Dockerfile .
   ````

2. Run the thing.

  ```{code-block} shell
  docker run -it -v $(pwd):/var/lib/test --name hr-test 
  ```
