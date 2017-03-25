Title: Histogrammar
Date: 2017-03-25 12:18
Slug: project_histogrammar.html
Authors: Jim Pivarski
Summary: Making histograms functional.

Histogrammar is a suite of data aggregation primitives for making histograms and much more. A few composable functions can generate many different types of plots, and these functions are reimplemented (exactly!) in multiple languages and serialized to JSON for cross-platform compatibility.

### Motivation

Histogrammar allows you to aggregate data using cross-platform, functional primitives. It serves the same need as HBOOK and its descendants— summarizing a large dataset with discretized distributions— but it does so using lambda functions and composition rather than a restrictive set of histogram types.

This simplifies many problems in data analysis (when the user wants to aggregate something that isn't exactly a traditional histogram), but it also fits nicely into functional environments like Apache Spark.

### Technique

The [Histogrammar specification](http://histogrammar.org/docs/specification/1.0/) describes a set of 19 aggregation functions that can be nested within each other. For instance, “Count” can be nested within “Bin” to make a one-dimensional histogram, or that can be nested within another “Bin” to make a two-dimensional histogram. All of these aggregation functions share mathematical properties (linear monoids) that allow them to be aggregated in parallel and then combined.

Each aggregation function is specified in a language-neutral way and has a JSON format for interchanging objects between languages.

Specific language implementations can additionally implement convenience functions for filling (back-ends) or plotting (front-ends), thus tying Histogrammar to existing data manipulation tools and visualization frameworks.

### Status

The Python and Scala implementations are the most complete, with dabblings in other languages. Users are contributing bug patches and convenience functions, and some developers have been writing other language versions on their own (Haskell, Elm, and Elixir).

### More information

A very detailed description is given on the Histogrammar website: [http://histogrammar.org](http://histogrammar.org)
