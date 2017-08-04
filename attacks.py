from Actions import Attack, SpellAttack

short_sword_slash = Attack(name="Short Sword",
                           stat_bonus="STR",
                           save=None,
                           damage={6: 1})

mace_hit = Attack(name="Mace",
                  stat_bonus="STR",
                  save=None,
                  damage={8: 1})

scorching_ray = SpellAttack(name="Scorching Ray",
                            stat_bonus="INT",
                            save=None,
                            damage={6: 2},
                            num_available=2,
                            multi_attack=3)

magic_missile = SpellAttack(name="Magic Missile",
                            stat_bonus="None",
                            save=None,
                            damage={4: 1},
                            num_available=4,
                            bonus_to_hit=1000,
                            bonus_to_damage=1,
                            multi_attack=3)

acid_splash = SpellAttack(name="Acid Splash",
                          stat_bonus=None,
                          save={"stat": "DEX", "DC": 13},
                          damage={6: 1})

sacred_flame = SpellAttack(name="Sacred Flame",
                           stat_bonus=None,
                           save={"stat": "DEX", "DC": 13},
                           damage={8: 1})
