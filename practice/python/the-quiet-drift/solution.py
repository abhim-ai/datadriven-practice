def reconcile(source_a: list[dict], source_b: list[dict], id_field: str) -> dict:
  """
  Cases to handle:
  id the records which match
  id record in which field values dont match
  id records only in either sources
  KV pairs which dont exist
  KV which exist
  """
  result = {"only_a": [], "only_b": [], "matches": [], "mismatches": []}
  records_a = {} #{1:{"id":1,"amount":100,"status":"posted"}}
  records_b = {}
  # Index the records by the id field
  for record in source_a:
    records_a[record[id_field]]=record
  for record in source_b:
    records_b[record[id_field]]=record

  # get all ids
  all_ids = set(records_a) | set(records_b)
  # iterate all over ids
  for id in sorted(all_ids):
    # check if its not in a, not in b, else check for differences the matches and mismatches
    if id not in records_b:
      result["only_a"].append(id)
    elif id not in records_a:
      result["only_b"].append(id)
    else:
      differences = diff_check(records_a[id], records_b[id], id_field)
      if differences:
        result["mismatches"].append({"id": id, "differences": differences})
      else:
        result["matches"].append(id)
  return result


# def diff_check(rec_a: dict, rec_b: dict, id_field: str) -> dict:
#   differences = {}
#   all_fields = set(rec_a) | set(rec_b)
#   all_fields.discard(id_field)
#   for field in all_fields:
#     if field not in rec_a:
#       if rec_b[field] is not None:
#         differences[field] = {"a": None, "b": rec_b[field]}
#     elif field not in rec_b:
#       if rec_a[field] is not None:
#         differences[field] = {"a": rec_a[field], "b": None}
#     elif rec_a[field] != rec_b[field]:
#       differences[field] = {"a": rec_a[field], "b": rec_b[field]}
#   return differences
def diff_check(record_a: dict, record_b: dict, id_field: str) -> dict:
  differences = {}
  all_fields = set(record_a) | set(record_b)
  all_fields.discard(id_field)
  for field in all_fields:
    value_a = record_a.get(field)
    value_b = record_b.get(field)
    if value_a != value_b:
      differences[field] = {"a": value_a, "b": value_b}
  return differences
