import FWCore.ParameterSet.Config as cms

particleFlow = cms.EDProducer("FSPFProducer",
                                # PFCandidate label
                                pfCandidates = cms.InputTag("particleFlowBeforePatch"),
                                par1 = cms.double(0.145),
                                par2 = cms.double(0.0031),
                                barrel_th = cms.double(0.8),
                                middle_th = cms.double(1.1),                             
                                endcap_th = cms.double(2.4)
                                )



