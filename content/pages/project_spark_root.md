Title: Spark-ROOT
Date: 2017-03-25 12:36
Slug: project_spark_root.html
Authors: Jim Pivarski
Summary: Access ROOT data in Apache Spark.

Spark-ROOT is a pure-Java (and Scala) implementation of ROOT file reading, which presents a collection of ROOT files as a DataFrame object in Spark. This allows high-energy physicists to use Spark without giving up on or reformatting all their data.

### Motivation

Spark is a useful platform for data analysis. It provides easy access to parallelization and is a focus point for data science tools from industry, particularly machine learning.

However, none of this would be useful to high-energy physicists if they cannot get their data into the platform. Spark-ROOT does this transparently.

### Technique

Spark-ROOT is not a JNI adaptation of ROOT or even a socket or pipe-based bridge. It is a reimplementation of ROOT file reading based on Tony Johnson's FreeHEP project. As a pure-Java project, it is trivial to install (see below) and doesn't suffer from segmentation faults in the JNI or the flimsiness of piping data to an external process.

ROOT's ability to selectively read columns is matched to Spark's "pruned scan" to automatically optimize reads.

ROOT files may be accessed locally or from HDFS.

### How to use

When you launch Spark, pass Spark-ROOT's Maven coordinates to load the package on startup.

    spark-shell --packages org.diana-hep:spark-root_2.11:0.1.7

Now you can

    import org.dianahep.sparkroot._
    val df = spark.sqlContext.read.root("path/to/file.root")

and use `df` as you would any other Spark DataFrame.

### For more information

See the GitHub site: [http://github.com/diana-hep/spark-root](http://github.com/diana-hep/spark-root).

