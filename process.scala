import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD

//Load the adjacency list into a graph
val graph = GraphLoader.edgeListFile(sc, "///example/adlist.txt")
//find the ranks over 25 iterations
val ranks = graph.staticPageRank(25).vertices

//read in the titles
val titles = sc.textFile("///example/titles.txt").map { line =>
  val fields = line.split(" ")
  (fields(0).toLong, fields(1))
}

//join the titles and ranks
val ranksByTitle = titles.join(ranks).map {
  case (id, (title, rank)) => (title, rank)
}
//print to stdout
println(ranksByTitle.collect().mkString("\n"))

//ranks.collect().foreach(println)
~                                    
