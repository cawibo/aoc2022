import scala.io.Source

object CalorieCounting {
  @main def main(task: Int*) =
    task match
      case Seq(1) => part1()
      case Seq(2) => part2()
      case _      => part1(); println; part2()

  def part1() = {
    println(solve("ex1"))
    println(solve("1"))
  }

  def part2() =
    println(solve("ex1", 3))
    println(solve("1", 3))

  def solve(task: String, top: Int = 1): Int =
    Source
      .fromFile(task)
      .mkString
      .split("\n\n")
      .map(_.split("\n").map(_.toInt).sum)
      .sorted(Ordering.Int.reverse)
      .take(top)
      .sum
}
