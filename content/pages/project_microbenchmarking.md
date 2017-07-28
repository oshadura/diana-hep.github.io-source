Title: Microbenchmarking and performance unit testing for ROOT
Date: 2017-07-28 12:00
Slug: project_microbenchmarking.html
Authors: Oksana Shadura, Vassil Vassilev
Summary: ROOT Vectorization and IO Benchmarking

### Performance unit testing (Google Benchmark)

Google Benchmark is a library to support the benchmarking of functions, similar to unit-tests. As main functionality, Google  benchmark provide a micro benchmark framework with possibility to change arguments and ranges, to use templated benchmarks, providing reports in csv and json output formats and using multithreading support.


### Vectorization benchmarks

<p align="center">
  <img src="../images/project_benchmarking/Cartesian3Dchart.jpeg" height="40%" width="40%">
  <br><b>Figure 1. Microbenchmarking of Cartesian3D benchmarks</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/GenVgccchart.jpeg" height="40%" width="40%">
  <br><b>Figure 2. Microbenchmarking of GenVectorVc benchmark in KNL (gcc6.2)</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/GenViccchart.jpeg" height="40%" width="40%">
  <br><b>Figure 3. Microbenchmarking of GenVectorVc benchmark in KNL (ICC17)</b><br>
</p>

### IO benchmarks

<p align="center">
  <img src="../images/project_benchmarking/IOchart.jpeg" height="40%" width="40%">
  <br><b>Figure 4. Microbenchmarking IO depending of size of AutoFlush for TBufferMerger on KNL</b><br>
</p>