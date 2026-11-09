import csv,unittest
class MappingTests(unittest.TestCase):
 def test_shared_provider_and_unverified_flags(self):
  with open("data/dependencies.csv",newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
  from dependency_poc.core import analyze
  report,graph=analyze(rows)
  self.assertEqual(len(report),5)
  self.assertEqual(len(graph),5)
  self.assertEqual(graph["Northstar Cloud"],["SVC-01","SVC-02","SVC-03","SVC-04"])
  self.assertIn("SHARED_PROVIDER_REVIEW",report[0]["review_flags"])
  self.assertIn("VERIFY_DEPENDENCIES",report[1]["review_flags"])
 def test_single_service_provider_not_shared(self):
  from dependency_poc.core import analyze
  report,graph=analyze([{"service_id":"A","service_name":"A","providers":"OnlyCo","verification":"confirmed"}])
  self.assertEqual(report[0]["review_flags"],"NONE")
  self.assertEqual(graph,{"OnlyCo":["A"]})
if __name__=="__main__":unittest.main()
