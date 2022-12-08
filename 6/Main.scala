import scala.io.Source

object TuningTrouble {
  @main def main(task: Int*) =
    task match 
      case Seq(1) => part1()
      case Seq(2) => part2()
      case _ => part1(); part2()

  def part1() = {
    println(solve("ex1", 4))
    println(solve("1", 4))
  }

  def part2() =
    println(solve("ex1", 14))
    println(solve("1", 14))

  def solve(task: String, window: Int): Int =
    Source
      .fromFile(task)
      .sliding(window)
      .indexWhere(_.distinct.size == window) + window
}
