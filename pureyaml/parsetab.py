
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '3F088763170081BD5E15FE873DB3844A'
    
_lr_action_items = {'DOUBLE_QUOTE':([0,1,2,4,5,6,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,30,],[2,-16,2,2,-15,-10,-9,-7,-6,2,-21,2,2,-14,26,2,2,2,-12,-20,-17,-22,-13,-8,2,-19,]),'CAST_INDICATOR':([0,1,2,4,5,6,8,9,10,11,13,14,15,16,18,19,20,21,22,23,25,26,27,28,30,],[3,-16,3,3,-15,-10,-9,-7,-6,3,-21,3,3,-14,3,3,3,-12,-20,-17,-22,-13,-8,3,-19,]),'DOC_START_INDICATOR':([0,1,5,6,8,9,10,11,13,14,16,19,21,22,23,25,26,27,28,30,],[4,-16,-15,-10,-9,-7,-6,-11,-21,-18,-14,4,-12,-20,-17,-22,-13,-8,4,-19,]),'INT':([0,1,2,4,5,6,8,9,10,11,13,14,15,16,18,19,20,21,22,23,25,26,27,28,30,],[6,-16,6,6,-15,-10,-9,-7,-6,6,-21,6,6,-14,6,6,6,-12,-20,-17,-22,-13,-8,6,-19,]),'FLOAT':([0,1,2,4,5,6,8,9,10,11,13,14,15,16,18,19,20,21,22,23,25,26,27,28,30,],[8,-16,8,8,-15,-10,-9,-7,-6,8,-21,8,8,-14,8,8,8,-12,-20,-17,-22,-13,-8,8,-19,]),'MAP_INDICATOR':([6,8,10,11,16,21,24,26,27,],[-10,-9,20,-11,-14,-12,20,-13,-8,]),'DOC_END_INDICATOR':([1,5,6,8,9,10,11,13,14,16,19,21,22,23,25,26,27,30,],[-16,-15,-10,-9,-7,-6,-11,-21,-18,-14,28,-12,-20,-17,-22,-13,-8,-19,]),'CAST_TYPE':([3,],[18,]),'SEQUENCE_INDICATOR':([0,1,4,5,6,8,9,10,11,13,14,16,19,21,22,23,25,26,27,28,30,],[15,-16,15,-15,-10,-9,-7,-6,-11,15,-18,-14,15,-12,-20,-17,-22,-13,-8,15,-19,]),'BOOL':([0,1,2,4,5,6,8,9,10,11,13,14,15,16,18,19,20,21,22,23,25,26,27,28,30,],[11,-16,11,11,-15,-10,-9,-7,-6,11,-21,11,11,-14,11,11,11,-12,-20,-17,-22,-13,-8,11,-19,]),'$end':([1,5,6,7,8,9,10,11,12,13,14,16,19,21,22,23,25,26,27,28,29,30,31,],[-16,-15,-10,0,-9,-7,-6,-11,-5,-21,-18,-14,-4,-12,-20,-17,-22,-13,-8,-3,-2,-19,-1,]),'STRING':([0,1,2,4,5,6,8,9,10,11,13,14,15,16,18,19,20,21,22,23,25,26,27,28,30,],[16,-16,16,16,-15,-10,-9,-7,-6,16,-21,16,16,-14,16,16,16,-12,-20,-17,-22,-13,-8,16,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'map':([0,4,14,19,28,],[1,1,23,1,1,]),'sequence':([0,4,13,19,28,],[5,5,22,5,5,]),'doc':([0,4,19,28,],[12,19,12,12,]),'collection':([0,4,19,28,],[9,9,9,9,]),'scalar':([0,2,4,11,14,15,18,19,20,28,],[10,17,10,21,24,25,27,10,30,10,]),'docs':([0,19,28,],[7,29,31,]),'sequence_item':([0,4,13,19,28,],[13,13,13,13,13,]),'map_item':([0,4,14,19,28,],[14,14,14,14,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> docs","S'",1,None,None,None),
  ('docs -> DOC_START_INDICATOR doc DOC_END_INDICATOR docs','docs',4,'p_docs_init','pureyaml.py',74),
  ('docs -> DOC_START_INDICATOR doc docs','docs',3,'p_docs_init','pureyaml.py',75),
  ('docs -> DOC_START_INDICATOR doc DOC_END_INDICATOR','docs',3,'p_docs_last','pureyaml.py',87),
  ('docs -> DOC_START_INDICATOR doc','docs',2,'p_docs_last','pureyaml.py',88),
  ('docs -> doc','docs',1,'p_docs_implicit','pureyaml.py',95),
  ('doc -> scalar','doc',1,'p_doc','pureyaml.py',102),
  ('doc -> collection','doc',1,'p_doc','pureyaml.py',103),
  ('scalar -> CAST_INDICATOR CAST_TYPE scalar','scalar',3,'p_scalar_explicit_cast','pureyaml.py',110),
  ('scalar -> FLOAT','scalar',1,'p_scalar_float','pureyaml.py',121),
  ('scalar -> INT','scalar',1,'p_scalar_int','pureyaml.py',129),
  ('scalar -> BOOL','scalar',1,'p_scalar_bool','pureyaml.py',137),
  ('scalar -> BOOL scalar','scalar',2,'p_scalar_disambiguous_string','pureyaml.py',143),
  ('scalar -> DOUBLE_QUOTE scalar DOUBLE_QUOTE','scalar',3,'p_scalar_string_double_quote','pureyaml.py',149),
  ('scalar -> STRING','scalar',1,'p_scalar_string','pureyaml.py',156),
  ('collection -> sequence','collection',1,'p_collection','pureyaml.py',163),
  ('collection -> map','collection',1,'p_collection','pureyaml.py',164),
  ('map -> map_item map','map',2,'p_map_init','pureyaml.py',171),
  ('map -> map_item','map',1,'p_map_last','pureyaml.py',178),
  ('map_item -> scalar MAP_INDICATOR scalar','map_item',3,'p_map_item','pureyaml.py',185),
  ('sequence -> sequence_item sequence','sequence',2,'p_sequence_init','pureyaml.py',192),
  ('sequence -> sequence_item','sequence',1,'p_sequence_last','pureyaml.py',199),
  ('sequence_item -> SEQUENCE_INDICATOR scalar','sequence_item',2,'p_sequence_item','pureyaml.py',206),
]
