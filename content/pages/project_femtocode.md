Title: Femtocode
Date: 2017-03-25 12:10
Slug: project_femtocode.html
Authors: Jim Pivarski
Summary: Quick manipulation of structured data for data analysis.

Femtocode is a language and a system to support fast queries on structured data, such as high-energy physics data.

### Motivation

The goal of this project is to replace the practice of copying and reducing a centrally produced dataset with direct queries on that dataset. Currently, high-energy physicists write programs to extract the attributes and data records of interest— personally managing the storage and versioning of that private copy— just to make plots from the subset in real time. Femtocode will allow users to make plots from the original dataset in real time, which may be as large as petabytes.

### Technique

Femtocode makes this possible by introducing a novel translation of query semantics into pure array operations, which strips away all unnecessary work at runtime. By dramatically reducing the computation time, the only bottleneck left is the data transfer, so caching is also heavily used to minimize the impact of repeated and similar queries.

### Status

This project is at an early stage of its development, though it is past the feasibility studies and basic implementation. End-to-end demonstrations will be possible by the end of April and usable prototypes will be available sometime in the summer of 2017.

### More information

A very detailed description is given on the Femtocode GitHub page: [http://github.com/diana-hep/femtocode](http://github.com/diana-hep/femtocode)
