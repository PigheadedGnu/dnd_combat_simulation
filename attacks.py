from Actions import Attack, SpellAttack

short_sword_slash = Attack(name="Short Sword",
                           stat_bonus="STR",
                           save=None,
                           damage={6: 1},
                           recharge_percentile=0.0,
                           num_available=-1)

mace_hit = Attack(name="Mace",
                  stat_bonus="STR",
                  save=None,
                  damage={8: 1},
                  recharge_percentile=0.0,
                  num_available=-1)

scorching_ray = SpellAttack(name="Scorching Ray",
                            stat_bonus="INT",
                            save=None,
                            damage={6: 2},
                            recharge_percentile=0.0,
                            num_available=2,
                            multi_attack=3)

sacred_flame = SpellAttack(name="Sacred Flame",
                           stat_bonus=None,
                           save={"stat": "DEX", "DC": 13},
                           damage={8: 1},
                           recharge_percentile=0.0,
                           num_available=-1)
