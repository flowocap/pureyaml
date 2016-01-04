
# _parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '91702DED7199ECBC96073B39F67162A3'
    
_lr_action_items = {'DEDENT':([1,3,5,6,8,12,14,15,17,18,20,22,23,25,30,],[-13,-24,-12,-22,-21,-23,-18,-15,26,27,-20,-17,-14,-19,-16,]),'INDENT':([0,1,3,4,5,6,8,9,11,12,14,15,17,18,19,20,22,23,25,26,27,28,30,],[2,-13,-24,2,-12,-22,-21,-6,-7,-23,-18,-15,-9,-11,2,-20,-17,-14,-19,-8,-10,2,-16,]),'STRING':([0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,25,26,27,28,30,],[3,-13,3,-24,3,-12,-22,-21,-6,3,-7,-23,-18,3,3,-9,-11,3,-20,3,-17,-14,-19,-8,-10,3,-16,]),'DOC_START_INDICATOR':([0,1,3,5,6,8,9,11,12,14,15,17,18,19,20,22,23,25,26,27,28,30,],[4,-13,-24,-12,-22,-21,-6,-7,-23,-18,-15,-9,-11,4,-20,-17,-14,-19,-8,-10,4,-16,]),'INT':([0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,25,26,27,28,30,],[6,-13,6,-24,6,-12,-22,-21,-6,6,-7,-23,-18,6,6,-9,-11,6,-20,6,-17,-14,-19,-8,-10,6,-16,]),'FLOAT':([0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,25,26,27,28,30,],[8,-13,8,-24,8,-12,-22,-21,-6,8,-7,-23,-18,8,8,-9,-11,8,-20,8,-17,-14,-19,-8,-10,8,-16,]),'MAP_INDICATOR':([3,6,8,11,12,18,20,24,],[-24,-22,-21,21,-23,21,-20,21,]),'DOC_END_INDICATOR':([1,3,5,6,8,9,11,12,14,15,17,18,19,20,22,23,25,26,27,30,],[-13,-24,-12,-22,-21,-6,-7,-23,-18,-15,-9,-11,28,-20,-17,-14,-19,-8,-10,-16,]),'CAST_TYPE':([0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,25,26,27,28,30,],[10,-13,10,-24,10,-12,-22,-21,-6,10,-7,-23,-18,10,10,-9,-11,10,-20,10,-17,-14,-19,-8,-10,10,-16,]),'SEQUENCE_INDICATOR':([0,1,2,3,4,5,6,8,9,11,12,14,15,17,18,19,20,22,23,25,26,27,28,30,],[16,-13,16,-24,16,-12,-22,-21,-6,-7,-23,16,-15,-9,-11,16,-20,-17,-14,-19,-8,-10,16,-16,]),'BOOL':([0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,25,26,27,28,30,],[12,-13,12,-24,12,-12,-22,-21,-6,12,-7,-23,-18,12,12,-9,-11,12,-20,12,-17,-14,-19,-8,-10,12,-16,]),'$end':([1,3,5,6,7,8,9,11,12,13,14,15,17,18,19,20,22,23,25,26,27,28,29,30,31,],[-13,-24,-12,-22,0,-21,-6,-7,-23,-5,-18,-15,-9,-11,-4,-20,-17,-14,-19,-8,-10,-3,-2,-16,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'map':([0,2,4,15,19,28,],[1,1,1,23,1,1,]),'sequence':([0,2,4,14,19,28,],[5,5,5,22,5,5,]),'doc':([0,4,19,28,],[13,19,13,13,]),'collection':([0,2,4,19,28,],[9,17,9,9,9,]),'scalar':([0,2,4,10,15,16,19,21,28,],[11,18,11,20,24,25,11,30,11,]),'docs':([0,19,28,],[7,29,31,]),'sequence_item':([0,2,4,14,19,28,],[14,14,14,14,14,14,]),'map_item':([0,2,4,15,19,28,],[15,15,15,15,15,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> docs","S'",1,None,None,None),
  ('docs -> DOC_START_INDICATOR doc DOC_END_INDICATOR docs','docs',4,'p_docs_init','grammar.py',230),
  ('docs -> DOC_START_INDICATOR doc docs','docs',3,'p_docs_init','grammar.py',231),
  ('docs -> DOC_START_INDICATOR doc DOC_END_INDICATOR','docs',3,'p_docs_last','grammar.py',257),
  ('docs -> DOC_START_INDICATOR doc','docs',2,'p_docs_last','grammar.py',258),
  ('docs -> doc','docs',1,'p_docs_implicit','grammar.py',264),
  ('doc -> collection','doc',1,'p_doc','grammar.py',270),
  ('doc -> scalar','doc',1,'p_doc','grammar.py',271),
  ('doc -> INDENT collection DEDENT','doc',3,'p_doc_indent','grammar.py',277),
  ('doc -> INDENT collection','doc',2,'p_doc_indent','grammar.py',278),
  ('doc -> INDENT scalar DEDENT','doc',3,'p_doc_indent','grammar.py',279),
  ('doc -> INDENT scalar','doc',2,'p_doc_indent','grammar.py',280),
  ('collection -> sequence','collection',1,'p_collection','grammar.py',286),
  ('collection -> map','collection',1,'p_collection','grammar.py',287),
  ('map -> map_item map','map',2,'p_map_init','grammar.py',293),
  ('map -> map_item','map',1,'p_map_last','grammar.py',299),
  ('map_item -> scalar MAP_INDICATOR scalar','map_item',3,'p_map_item','grammar.py',305),
  ('sequence -> sequence_item sequence','sequence',2,'p_sequence_init','grammar.py',311),
  ('sequence -> sequence_item','sequence',1,'p_sequence_last','grammar.py',317),
  ('sequence_item -> SEQUENCE_INDICATOR scalar','sequence_item',2,'p_sequence_item','grammar.py',323),
  ('scalar -> CAST_TYPE scalar','scalar',2,'p_scalar_explicit_cast','grammar.py',329),
  ('scalar -> FLOAT','scalar',1,'p_scalar_float','grammar.py',336),
  ('scalar -> INT','scalar',1,'p_scalar_int','grammar.py',343),
  ('scalar -> BOOL','scalar',1,'p_scalar_bool','grammar.py',350),
  ('scalar -> STRING','scalar',1,'p_scalar_string','grammar.py',362),
]