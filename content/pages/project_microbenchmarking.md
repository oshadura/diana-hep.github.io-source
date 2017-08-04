Title: Microbenchmarking and performance unit testing for ROOT
Date: 2017-07-28 12:00
Slug: project_microbenchmarking.html
Authors: Oksana Shadura
Under supervision of Dr. Brian Bockelman and Dr. Vassil Vassilev
Summary: ROOT Vectorization and IO Benchmarking

### Performance unit testing (Google Benchmark)

Google Benchmark is a library to support the benchmarking of functions, similar to unit-tests. As main functionality, Google  benchmark provide a micro benchmark framework with possibility to change arguments and ranges, to use templated benchmarks, providing reports in csv and json output formats and using multithreading support.


### Vectorization benchmarks

<p align="center">
  <img src="../images/project_benchmarking/Cartesian3Dchart.jpeg" height="100%" width="100%">
  <br><b>Figure 1. Microbenchmarking of Cartesian3D benchmarks</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/GenVgccchart.jpeg" hheight="100%" width="100%>
  <br><b>Figure 2. Microbenchmarking of GenVectorVc benchmark in KNL (gcc6.2)</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/GenViccchart.jpeg"height="100%" width="100%>
  <br><b>Figure 3. Microbenchmarking of GenVectorVc benchmark in KNL (ICC17)</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/GCCGenVecchart.jpeg" height="100%" width="100%>
  <br><b>Figure 2. Speedup of GenVectorVc benchmark in KNL (gcc6.2)</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/ICCGenVecchart.jpeg" height="100%" width="100%>
  <br><b>Figure 3. Speedup of GenVectorVc benchmark in KNL (ICC17)</b><br>
</p>

### IO benchmarks

<p align="center">
  <img src="../images/project_benchmarking/IOchart_128.jpeg" height="100%" width="100%>
  <br><b>Figure 4. Microbenchmarking IO depending of size of AutoFlush for TBufferMerger on KNL</b><br>
</p>

<p align="center">
  <img src="../images/project_benchmarking/KNLTFile1Branch.jpeg" height="100%" width="100%>
  <br><b>Figure 4. Microbenchmarking IO depending of size of AutoFlush for TBufferMerger on KNL for 1 Branch</b><br>
</p>