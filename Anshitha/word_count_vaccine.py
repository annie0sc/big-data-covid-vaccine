from pyflink.dataset import ExecutionEnvironment
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import (
    TableConfig,
    DataTypes,
    BatchTableEnvironment,
    StreamTableEnvironment,
)
from pyflink.table.descriptors import Schema, Csv, OldCsv, FileSystem
from pathlib import Path

exec_env = ExecutionEnvironment.get_execution_environment()
exec_env.set_parallelism(1)
t_config = TableConfig()
t_env = BatchTableEnvironment.create(exec_env, t_config)
root = Path("vaccinations.csv").parent.resolve()
out_path = root / "output_vaccines.csv"

try:
    out_path.unlink()
except:
    pass

from pyflink.table.window import Tumble

(
    t_env.connect(FileSystem().path(str(root / "vaccinations.csv")))
    .with_format(Csv())
    .with_schema(
        Schema().field("date", DataTypes.DATE(True)).field("word", DataTypes.STRING())
    )
    .create_temporary_table("mySource")
)

(
    t_env.connect(FileSystem().path(str(out_path)))
    .with_format(Csv())
    .with_schema(
        Schema().field("word", DataTypes.STRING()).field("count", DataTypes.BIGINT())
    )
    .create_temporary_table("mySink")
)

(
    t_env.from_path("mySource")
    .group_by("word")
    .select("word, count(1) as count")
    .filter("count > 1")
    .insert_into("mySink")
)

t_env.execute("word_count_vaccine")