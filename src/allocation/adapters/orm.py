import logging
from sqlalchemy import (
    Table,
<<<<<<< HEAD
    MetaData,
=======
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    event,
)
<<<<<<< HEAD
from sqlalchemy.orm import mapper, relationship
=======
from sqlalchemy.orm import registry, relationship
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693

from allocation.domain import model

logger = logging.getLogger(__name__)

<<<<<<< HEAD
metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
=======
mapper_registry = registry()

order_lines = Table(
    "order_lines",
    mapper_registry.metadata,
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False),
    Column("orderid", String(255)),
)

products = Table(
    "products",
<<<<<<< HEAD
    metadata,
=======
    mapper_registry.metadata,
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
    Column("sku", String(255), primary_key=True),
    Column("version_number", Integer, nullable=False, server_default="0"),
)

batches = Table(
    "batches",
<<<<<<< HEAD
    metadata,
=======
    mapper_registry.metadata,
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("reference", String(255)),
    Column("sku", ForeignKey("products.sku")),
    Column("_purchased_quantity", Integer, nullable=False),
    Column("eta", Date, nullable=True),
)

allocations = Table(
    "allocations",
<<<<<<< HEAD
    metadata,
=======
    mapper_registry.metadata,
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderline_id", ForeignKey("order_lines.id")),
    Column("batch_id", ForeignKey("batches.id")),
)

allocations_view = Table(
    "allocations_view",
<<<<<<< HEAD
    metadata,
=======
    mapper_registry.metadata,
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
    Column("orderid", String(255)),
    Column("sku", String(255)),
    Column("batchref", String(255)),
)


def start_mappers():
    logger.info("Starting mappers")
<<<<<<< HEAD
    lines_mapper = mapper(model.OrderLine, order_lines)
    batches_mapper = mapper(
=======
    lines_mapper = mapper_registry.map_imperatively(model.OrderLine, order_lines)
    batches_mapper = mapper_registry.map_imperatively(
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
        model.Batch,
        batches,
        properties={
            "_allocations": relationship(
                lines_mapper,
                secondary=allocations,
                collection_class=set,
            )
        },
    )
<<<<<<< HEAD
    mapper(
=======
    mapper_registry.map_imperatively(
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
        model.Product,
        products,
        properties={"batches": relationship(batches_mapper)},
    )


@event.listens_for(model.Product, "load")
def receive_load(product, _):
    product.events = []
